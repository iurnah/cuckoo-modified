# Copyright (C) 2015 Kevin Ross, Accuvant, Inc. (bspengler@accuvant.com)
# This file is part of Cuckoo Sandbox - http://www.cuckoosandbox.org
# See the file 'docs/LICENSE' for copying permission.

from lib.cuckoo.common.abstracts import Signature

class ModifySecurityCenterWarnings(Signature):
    name = "modify_security_center_warnings"
    description = "Attempts to modify or disable Security Center warnings"
    severity = 3
    categories = ["stealth"]
    authors = ["Kevin Ross", "Accuvant"]
    minimum = "1.2"

    def run(self):
        indicators = [
            ".*\\\\SOFTWARE\\\\(Wow6432Node\\\\)?Microsoft\\\\Security\\ Center\\\\.*",
            ".*\\\\SOFTWARE\\\\Microsoft\\\\Windows\\\\CurrentVersion\\\\explorer\\\\ShellServiceObjects\\\\{FD6905CE-952F-41F1-9A6F-135D9C6622CC}$",
        ]                                                                                                   
        for indicator in indicators:
            if self.check_write_key(pattern=indicator, regex=True):
                return True

        return False
