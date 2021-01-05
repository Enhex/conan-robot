from conans import ConanFile, tools

# automatically choose Premake generator
def run_premake(self):
	if "Visual Studio" in self.settings.compiler:
		_visuals = {'8': '2005',
					'9': '2008',
					'10': '2010',
					'11': '2012',
					'12': '2013',
					'14': '2015',
					'15': '2017',
					'16': '2019'}
		premake_command = "premake5 vs%s" % _visuals.get(str(self.settings.compiler.version), "UnknownVersion %s" % str(self.settings.compiler.version))
		self.run(premake_command)
	else:
		self.run("premake5 gmake")

class RobotConan(ConanFile):
    name = "robot"
    version = "master"
    license = "<Put the package license here>"
    author = "<Put your name here> <And your email here>"
    url = "<Package recipe repository url here, for issues about the package>"
    description = "<Description of Robot here>"
    topics = ("<Put some tag here>", "<here>", "<and here>")
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    generators = "premake"
    exports = "premake5.lua"

    def source(self):
        self.run("git clone --depth=1 https://github.com/Robot/robot.git")

    def build(self):
        run_premake(self)
        self.run("build")

    def package(self):
        self.copy("*.h", dst="include", src="robot/Source")
        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["Robot", "X11", "Xtst", "Xinerama"]