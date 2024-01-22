from .tika import detectLang1, callServer, ServerEndpoint

def from_file(filename, requestOptions={}):
    '''
    Detects language of the file
    :param filename: path to file whose language needs to be detected
    :return:
    '''
    jsonOutput = detectLang1('file', filename, requestOptions=requestOptions)
    return jsonOutput[1]

def from_buffer(string, requestOptions={}):
    '''
    Detects language of content in the buffer
    :param string: buffered data
    :return:
    '''
    status, response = callServer('put', ServerEndpoint, '/language/string', string,
                                  {'Accept': 'text/plain'}, False, requestOptions=requestOptions)
    return response
