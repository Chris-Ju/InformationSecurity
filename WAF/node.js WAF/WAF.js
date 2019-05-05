var fs= require("fs");

var level = 2;

var Filter = [
  'select', 'insert', 'update', 'delete', 'union', 'load_file', 'outfile', 'dumpfile', 'sub', 'hex', 'sleep', 'mid',
  '`', 'openlog', 'syslog', 'readlink', 'symlink', 'popepassthru', 'stream_socket_server', 'assert', 'pcntl_exec',
  'exec', 'system', 'chroot', 'scandir', 'chgrp', 'chown', 'shell_exec', 'proc_open', 'proc_get_status', 'popen', 'ini_alter', 'ini_restore', 'fget', 'file_get_contents', 'file_put_contents', 'fwrite', 'curl', 'system', 'eval', 'assert',
  'flag', 'getflag'
]



var WAF = (request) => {
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
  fs.appendFileSync('/tmp/waf.log', str)
  if (level >= 2) {
    dic_get_new = {}
    dic_post_new = {}
    for (var key in dic_get) {
      k_temp = key
      r_temp = dic_get[key]
      for (var i in Filter) {
        k_temp = k_temp.replace(Filter[i], 'fuck')
        r_temp = r_temp.replace(Filter[i], 'fuck')
      }
      dic_get_new[k_temp] = r_temp
    }
    request.query = dic_get_new
    for (var key in dic_post) {
      k_temp = key
      r_temp = dic_post[key]
      for (var i in Filter) {
        k_temp = k_temp.replace(Filter[i], 'fuck')
        r_temp = r_temp.replace(Filter[i], 'fuck')
      }
      dic_post_new[k_temp] = r_temp
    }
    request.body = dic_post_new
    console.log(dic_get_new)
    console.log(dic_post_new)
  }
  return request;
}

module.exports = WAF;