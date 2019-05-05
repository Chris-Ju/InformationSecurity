var fs= require("fs");

var RES = (request, response) => {
  if (response.indexOf('flag') != -1) {
    dic_get = request.query
    dic_post = request.body
    header = request.headers
    str = '----------\nip:\n' + request.ip +
      '\nGET:\n' + JSON.stringify(dic_get) +
      '\nPOST:\n' + JSON.stringify(dic_post) +
      '\nHEADER:\n'
    for (var key in header) {
      str += key + ': ' + header[key] + '\n'
    }
    str += '\n'
    fs.appendFileSync('/tmp/flag.log', str)
  }
}

module.exports = RES;