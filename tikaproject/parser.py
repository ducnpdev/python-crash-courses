from .tika import parse1, callServer, ServerEndpoint
import os
import json


def from_file(filename, serverEndpoint=ServerEndpoint, service='all', xmlContent=False, headers=None, config_path=None, requestOptions={}, raw_response=False):
    '''
    Parses a file for metadata and content
    :param filename: path to file which needs to be parsed or binary file using open(path,'rb')
    :param serverEndpoint: Server endpoint url
    :param service: service requested from the tika server
                    Default is 'all', which results in recursive text content+metadata.
                    'meta' returns only metadata
                    'text' returns only content
    :param xmlContent: Whether or not XML content be requested.
                    Default is 'False', which results in text content.
    :param headers: Request headers to be sent to the tika reset server, should
                    be a dictionary. This is optional
    :return: dictionary having 'metadata' and 'content' keys.
            'content' has a str value and metadata has a dict type value.
    '''
    if not xmlContent:
        output = parse1(service, filename, serverEndpoint, headers=headers, config_path=config_path, requestOptions=requestOptions)
    else:
        output = parse1(service, filename, serverEndpoint, services={'meta': '/meta', 'text': '/tika', 'all': '/rmeta/xml'},
                            headers=headers, config_path=config_path, requestOptions=requestOptions)
    if raw_response:
        return output
    else:
        return _parse(output, service)


def from_buffer(string, serverEndpoint=ServerEndpoint, xmlContent=False, headers=None, config_path=None, requestOptions={}, raw_response=False):
    '''
    Parses the content from buffer
    :param string: Buffer value
    :param serverEndpoint: Server endpoint. This is optional
    :param xmlContent: Whether or not XML content be requested.
                    Default is 'False', which results in text content.
    :param headers: Request headers to be sent to the tika reset server, should
                    be a dictionary. This is optional
    :return:
    '''
    headers = headers or {}
    headers.update({'Accept': 'application/json'})

    if not xmlContent:
        status, response = callServer('put', serverEndpoint, '/rmeta/text', string, headers, False, config_path=config_path, requestOptions=requestOptions)
    else:
        status, response = callServer('put', serverEndpoint, '/rmeta/xml', string, headers, False, config_path=config_path, requestOptions=requestOptions)

    if raw_response:
        return (status, response)
    else:
        return _parse((status,response))


def _parse(output, service='all'):
    '''
    Parses response from Tika REST API server
    :param output: output from Tika Server
    :param service: service requested from the tika server
                    Default is 'all', which results in recursive text content+metadata.
                    'meta' returns only metadata
                    'text' returns only content
    :return: a dictionary having 'metadata' and 'content' values
    '''
    parsed={'metadata': None, 'content': None}
    if not output:
        return parsed

    parsed["status"] = output[0]
    if output[1] == None or output[1] == "":
        return parsed

    if service == "text":
        parsed["content"] = output[1]
        return parsed

    realJson = json.loads(output[1])

    parsed["metadata"] = {}
    if service == "meta":
        for key in realJson:
            parsed["metadata"][key] = realJson[key]
        return parsed

    content = ""
    for js in realJson:
        if "X-TIKA:content" in js:
            content += js["X-TIKA:content"]

    if content == "":
        content = None

    parsed["content"] = content

    for js in realJson:
        for n in js:
            if n != "X-TIKA:content":
                if n in parsed["metadata"]:
                    if not isinstance(parsed["metadata"][n], list):
                        parsed["metadata"][n] = [parsed["metadata"][n]]
                    parsed["metadata"][n].append(js[n])
                else:
                    parsed["metadata"][n] = js[n]

    return parsed


# ---
from_file("rwservlet.pdf")