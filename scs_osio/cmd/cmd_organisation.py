"""
Created on 8 Mar 2017

@author: Bruno Beloff (bruno.beloff@southcoastscience.com)
"""

import optparse


# --------------------------------------------------------------------------------------------------------------------

class CmdOrganisation(object):
    """
    unix command line handler
    """

    def __init__(self):
        """
        Constructor
        """
        self.__parser = optparse.OptionParser(usage="%prog ORG_ID [-n NAME] [-w WEB] [-d DESCRIPTION] [-e EMAIL] [-v]",
                                              version="%prog 1.0")

        # optional...
        self.__parser.add_option("--name", "-n", type="string", nargs=1, action="store", dest="name",
                                 help="set name")

        self.__parser.add_option("--web", "-w", type="string", nargs=1, action="store", dest="website",
                                 help="set web URL")

        self.__parser.add_option("--desc", "-d", type="string", nargs=1, action="store", dest="description",
                                 help="set description")

        self.__parser.add_option("--email", "-e", type="string", nargs=1, action="store", dest="email",
                                 help="set email address")

        # optional...
        self.__parser.add_option("--verbose", "-v", action="store_true", dest="verbose", default=False,
                                 help="report narrative to stderr")

        self.__opts, self.__args = self.__parser.parse_args()


    # ----------------------------------------------------------------------------------------------------------------

    def is_valid(self):
        if self.org_id is None:
            return False

        return True


    # ----------------------------------------------------------------------------------------------------------------

    def set(self):
        return self.name is not None or self.website is not None or self.description is not None or \
               self.email is not None


    # ----------------------------------------------------------------------------------------------------------------

    @property
    def org_id(self):
        return self.__args[0] if len(self.__args) > 0 else None


    @property
    def name(self):
        return self.__opts.name


    @property
    def website(self):
        return self.__opts.website


    @property
    def description(self):
        return self.__opts.description


    @property
    def email(self):
        return self.__opts.email


    @property
    def verbose(self):
        return self.__opts.verbose


    @property
    def args(self):
        return self.__args


    # ----------------------------------------------------------------------------------------------------------------

    def print_help(self, file):
        self.__parser.print_help(file)


    def __str__(self, *args, **kwargs):
        return "CmdOrganisation:{org_id:%s, name:%s, website:%s, description:%s, email:%s, " \
               "verbose:%s, args:%s}" % \
                    (self.org_id, self.name, self.website, self.description, self.email,
                     self.verbose, self.args)
