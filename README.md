# Polydoro - Polybar Pomodoro #

Simple pomodoro timer for polybar.

## Install ##

1. Copy source to polybar config dir:

    ```bash
    git clone https://github.com/Radeox/polydoro.git ~/.config/polybar/polydoro/
    ```

2. Add the module to your configuration:

    ```bash
    include-file = ~/.config/polybar/polydoro/polydoro.ini

    ...

    modules-left = "... polydoro ..."
    ```

## Use ##

Left-click to start timer and right click to stop it.

### Optional ###

Check `config.py` to change timer duration.