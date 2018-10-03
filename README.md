# What is this
This is a nikola `shortcode` plugin made based on [notebook_shortcode](https://plugins.getnikola.com/#notebook_shortcode).

I changed the following.

- Fixed to get processing in nikola version 8.

- Plugin name: `notebook_shortcode` -> `jupyter_shortcode`
  - I don't like that name. (This is off the record, okay?)

- Origin in a path argument specified on `shortcode`.
  - This interprets a written path as the same directory the post file is put on.
  - That(original) interprets a written path as the project top directory.
    - You had to specify the path including parent directory if you use that.

# Usage

## Setup

1. Make a `plugins/` directory or the other one according to the config you specified. (e.g. `EXTRA_PLUGINS_DIRS`)
2. Put this plugin (this repository) on the plugins directory.

  ```bash
  $ git clone https://github.com/righ/nikola-jupyter-shortcode.git plugins/jupyter_shortcode
  ```

  You don't have to do the operation so far everytime.
  It is recommended committing the plugin as yours. (it does not matter that is git submodule or not)

3. You have to install dependencies manually unlike using `nikola plugin -i notebook_shortcode`.

  Installation: 

  ```bash
  $ pip install plugins/jupyter_shortcode/requirements.txt
  ```


## Description in a post

```
{{% raw %}}{{% jupyter ./notebook.ipynb %}}{{% /raw %}}
```
(`raw` block may be unnecessary)

Good luck 👍

# Original document

This plugin inserts a Jupyter/IPython notebook into a post using shortcode. This is useful, for example, when
adapting an existing notebook into a post with additional markup.

Usage:

```
{{% raw %}}{{% notebook path/to/notebook.ipynb %}}{{% /raw %}}
```

Note: `ipynb` must be enabled and configured (COMPILERS, POSTS/PAGES) for CSS to appear properly. If you are using math
in your notebook, make sure to add the `mathjax` tag to your post.
