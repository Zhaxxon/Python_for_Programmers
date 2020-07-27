import re
text = 'abcdfghijk'
parser = re.search('a[b-f]*f', text)
print (parser)
#<_sre.SRE_Match object; span=(0, 5), match='abcdf'>

print (parser.group())
#'abcdf'