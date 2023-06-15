{ pkgs }: {
  deps = [
    pkgs.ffmpeg.bin
    pkgs.zulu
    pkgs.chromedriver
    pkgs.chromium
    pkgs.python38Full
    pkgs.replitPackages.prybar-python3
    pkgs.chromedriver
  ];
  env = rec {
    PYTHON_LD_LIBRARY_PATH = pkgs.lib.makeLibraryPath [
      # Needed for pandas / numpy
      pkgs.stdenv.cc.cc.lib
      pkgs.zlib
      # Needed for pygame
      pkgs.glib
      # Needed for matplotlib
      pkgs.xorg.libX11
      pkgs.chromedriver
  ];
    PYTHONBIN = "${pkgs.python38Full}/bin/python3.8";
    LANG = "en_US.UTF-8";
  };
}