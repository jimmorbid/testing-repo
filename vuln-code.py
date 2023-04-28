#
# Lets write some vulnerable code!
# Semgrep tester
#

import commands
template_vars['output'] = commands.getstatusoutput('/usr/bin/process_soemthing')

hashed_password = hashlib.md5(request.params['foo']).hexdigest()

sh.semgrep("--config", "https://semgrep.dev/p/r2c-CI")

confurl = os.environ.get("SEMGREP_CONFIG_URL", "")
# ruleid: string-concat
sh.semgrep("--config {}".format(confurl))

# ruleid: string-concat
sh.semgrep(f"--config {confurl}")

# ok: string-concat
args = ["--config", confurl]
sh.semgrep(*args)