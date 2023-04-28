#
# Lets write some vulnerable code!
# Semgrep tester
#

import commands
template_vars['output'] = commands.getstatusoutput('/usr/bin/process_soemthing')

hashed_password = hashlib.md5(request.params['foo']).hexdigest()
