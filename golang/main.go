// -------------------

// package main

// import (
// 	"log"
// 	"time"

// 	"github.com/xitongsys/parquet-go-source/local"
// 	"github.com/xitongsys/parquet-go/parquet"
// 	"github.com/xitongsys/parquet-go/reader"
// 	"github.com/xitongsys/parquet-go/writer"
// )

// type Student struct {
// 	Name    string  `parquet:"name=name, type=BYTE_ARRAY, convertedtype=UTF8, encoding=PLAIN_DICTIONARY"`
// 	Age     int32   `parquet:"name=age, type=INT32, encoding=PLAIN"`
// 	Id      int64   `parquet:"name=id, type=INT64"`
// 	Weight  float32 `parquet:"name=weight, type=FLOAT"`
// 	Sex     bool    `parquet:"name=sex, type=BOOLEAN"`
// 	Day     int32   `parquet:"name=day, type=INT32, convertedtype=DATE"`
// 	Ignored int32   //without parquet tag and won't write
// }

// func main() {
// 	var err error
// 	fw, err := local.NewLocalFileWriter("file.parquet")
// 	if err != nil {
// 		log.Println("Can't create local file", err)
// 		return
// 	}

// 	//write
// 	pw, err := writer.NewParquetWriter(fw, new(Student), 4)
// 	if err != nil {
// 		log.Println("Can't create parquet writer", err)
// 		return
// 	}

// 	pw.RowGroupSize = 128 * 1024 * 1024 //128M
// 	pw.PageSize = 8 * 1024              //8K
// 	pw.CompressionType = parquet.CompressionCodec_SNAPPY
// 	num := 100
// 	for i := 0; i < num; i++ {
// 		stu := Student{
// 			Name:   "StudentName",
// 			Age:    int32(20 + i%5),
// 			Id:     int64(i),
// 			Weight: float32(50.0 + float32(i)*0.1),
// 			Sex:    bool(i%2 == 0),
// 			Day:    int32(time.Now().Unix() / 3600 / 24),
// 		}
// 		if err = pw.Write(stu); err != nil {
// 			log.Println("Write error", err)
// 		}
// 	}
// 	if err = pw.WriteStop(); err != nil {
// 		log.Println("WriteStop error", err)
// 		return
// 	}
// 	log.Println("Write Finished")
// 	fw.Close()

// 	///read
// 	fr, err := local.NewLocalFileReader("file.parquet")
// 	if err != nil {
// 		log.Println("Can't open file")
// 		return
// 	}

// 	pr, err := reader.NewParquetReader(fr, new(Student), 4)
// 	if err != nil {
// 		log.Println("Can't create parquet reader", err)
// 		return
// 	}
// 	num = int(pr.GetNumRows())
// 	for i := 0; i < num/10; i++ {
// 		if i%2 == 0 {
// 			pr.SkipRows(10) //skip 10 rows
// 			continue
// 		}
// 		stus := make([]Student, 10) //read 10 rows
// 		if err = pr.Read(&stus); err != nil {
// 			log.Println("Read error", err)
// 		}
// 		log.Println(stus)
// 	}

// 	pr.ReadStop()
// 	fr.Close()

// }

package main

import (
	"context"
	"errors"
	"fmt"
	"os"
	"time"

	"github.com/aws/aws-sdk-go/aws"
	"github.com/aws/aws-sdk-go/aws/session"
	"github.com/aws/aws-sdk-go/service/s3"
	"github.com/aws/aws-sdk-go/service/s3/s3manager"
	"github.com/fraugster/parquet-go/floor"
	_ "github.com/fraugster/parquet-go/floor"
	"github.com/segmentio/ksuid"
	log "github.com/sirupsen/logrus"
)

var ErrIllegalRow = errors.New("row not fully formed")
var fileName = "file.parquet"

func main() {
	fmt.Println("main")
	ParseFile(fileName)

}

func DownloadFile(ctx context.Context, sess *session.Session, bucket string, key string) (string, error) {
	log.WithFields(log.Fields{
		"key":    key,
		"bucket": bucket,
	}).Debug("printing out the args")
	filePath := fmt.Sprintf("files/%s.parquet", ksuid.New().String())
	file, err := os.Create(filePath)

	if err != nil {
		return "", err
	}

	downloader := s3manager.NewDownloader(sess)
	_, err = downloader.DownloadWithContext(ctx, file,
		&s3.GetObjectInput{
			Bucket: aws.String(bucket),
			Key:    aws.String(key),
		})

	if err != nil {
		return "", err
	}

	return filePath, nil
}

func DeleteFile(fileName string) error {
	err := os.Remove(fileName)

	if err != nil {
		return err
	}

	return nil
}

type ParquetUser struct {
	Id             int       `json:"id"`
	FirstName      string    `json:"firstName"`
	LastName       string    `json:"lastName"`
	Role           string    `json:"QUOTE_TYPE"`
	Branch         string    `json:"BRANCH" parquet:"name=BRANCH, type=INT32"`
	EFFECTIVE_DATE string    `json:"EFFECTIVE_DATE"`
	LastUpdated    time.Time `json:"lastUpdated"`
}

func ParseFile(fileName string) ([]ParquetUser, error) {
	fr, err := floor.NewFileReader(fileName)
	var fileContent []ParquetUser
	if err != nil {
		return nil, err
	}

	// schema := fr.GetSchemaDefinition()
	// for _, column := range schema.SchemaElements {
	// 	fmt.Printf("Column Name: %s, Tag: %s\n", column.Name, column.GetTag())
	// }

	for fr.Next() {
		rec := &ParquetUser{}
		if err := fr.Scan(rec); err != nil {
			// continue along is it's just a malformed row
			if errors.Is(err, ErrIllegalRow) {
				fmt.Println("error")
				continue
			}
			return nil, err
		}
		fmt.Println("branch:", string(rec.Branch))
		fmt.Printf("%#v \n", rec)

		fileContent = append(fileContent, *rec)
	}
	// fmt.Println("fileConten /t:", fileContent)
	return fileContent, nil
}
