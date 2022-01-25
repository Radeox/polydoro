# Polydoro - Polybar Pomodoro #

Simple pomodoro timer for polybar.

## Install ##

1. Copy source to polybar config dir:

    ```bash
    git clone https://github.com/Radeox/polydoro.git ~/.config/polybar/polydoro/
    ```

2. Install required python modules:

    ```bash
    pip install -r ~/.config/polybar/polydoro/requirements.txt
    ```

3. Add the module to your configuration:

    ```bash
    include-file = ~/.config/polybar/polydoro/polydoro.ini

    ...

    modules-left = "... polydoro ..."
    ```

4. Restart polybar and use:

* `Left click` &rarr; Start timer
* `Right click` &rarr; Stop timer

### Optional ###

Check `config.py` to change timer duration.
