location_dir = "./"

include(location_dir .. "conanbuildinfo.premake.lua")

workspace("Robot")
	location(location_dir)
	conan_basic_setup()

	project("Robot")
		kind "StaticLib"
		language "C++"
		cppdialect "C++17"
		targetdir = location_dir .. "bin"

		files{
			"robot/Source/*.h",
			"robot/Source/*.cc"
		}

		filter "configurations:Debug"
			defines { "DEBUG" }
			symbols "On"

		filter "configurations:Release"
			defines { "NDEBUG" }
			optimize "On"