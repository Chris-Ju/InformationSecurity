B = (function x() {})[-5] == 'x'?
'FF3' : (function x() {})[-6] == 'x'?
'FF2' : /a/[-1] == 'a'?
'FF'  : '\v' == 'v'?
'IE'  : /a/.__proto__ == '//'?
'Saf' : /s/.test(/a/.toString)?
'Chr' : /^function \(/.test([].sort)?
'Op'  : 'Unknown'