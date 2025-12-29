
{ pkgs, ... }: {
  channel = "stable-24.05";
  packages = [
    pkgs.python3
    pkgs.python3Packages.pip
    pkgs.python3Packages.flask  # Added Flask package
  ];
  env = {};
  idx = {
    extensions = [
      "ms-python.python"
      "google.gemini-cli-vscode-ide-companion"
    ];
    previews = {
      enable = true;
      previews = {
        web = {
          command = ["flask" "run" "--port" "$PORT"];
          manager = "web";
        };
      };
    };
    workspace = {
      onCreate = {
        pip-install = "pip install -r requirements.txt";
        default.openFiles = [ ".idx/dev.nix" "README.md" "app.py" ];
      };
      onStart = {};
    };
  };
}
