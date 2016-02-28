# Markdown Compatibility

Basically taken from http://learn.getgrav.org/content/markdown


kramdown
: A Markdown-superset converter

markdown
: Super awesome, tasty markup language

Footnotes[^1] have a label[^@#$%] and the footnote's content.

[^1]: This is a footnote content.
[^@#$%]: A footnote on the label: "@#$%".

## h2 Heading
### h3 Heading
#### h4 Heading
##### h5 Heading
###### h6 Heading


**rendered as bold text**


_rendered as italicized text_


~~Strike through this text.~~


> **Fusion Drive** combines a hard drive with a flash storage (solid-state drive) and presents it as a single logical volume with the space of both drives combined.


* valid bullet
- valid bullet
+ valid bullet


1. Lorem ipsum dolor sit amet
2. Consectetur adipiscing elit
3. Integer molestie lorem at massa
4. Facilisis in pretium nisl aliquet
5. Nulla volutpat aliquam velit
6. Faucibus porta lacus fringilla vel
7. Aenean sit amet erat nunc
8. Eget porttitor lorem


1. Lorem ipsum dolor sit amet
1. Consectetur adipiscing elit
1. Integer molestie lorem at massa
1. Facilisis in pretium nisl aliquet
1. Nulla volutpat aliquam velit
1. Faucibus porta lacus fringilla vel
1. Aenean sit amet erat nunc
1. Eget porttitor lorem


In this example, `<section></section>` should be wrapped as **code**.

``` markup
Sample text here...
```

```js
grunt.initConfig({
  assemble: {
    options: {
      assets: 'docs/assets',
      data: 'src/data/*.{json,yml}',
      helpers: 'src/custom-helpers.js',
      partials: ['src/partials/**/*.{hbs,md}']
    },
    pages: {
      options: {
        layout: 'default.hbs'
      },
      files: {
        './': ['src/templates/pages/index.hbs']
      }
    }
  }
};
```


| Option | Description |
| ------ | ----------- |
| data   | path to data files to supply the data that will be passed into templates. |
| engine | engine to be used for processing templates. Handlebars is the default. |
| ext    | extension to be used for dest files. |


| Option | Description |
| ------:| -----------:|
| data   | path to data files to supply the data that will be passed into templates. |
| engine | engine to be used for processing templates. Handlebars is the default. |
| ext    | extension to be used for dest files. |

[Assemble](http://assemble.io)

[Upstage](https://github.com/upstage/ "Visit Upstage!")

![Minion](http://octodex.github.com/images/minion.png)

![Alt text](http://octodex.github.com/images/stormtroopocat.jpg "The Stormtroopocat")

![Alt text][id]

[id]: http://octodex.github.com/images/dojocat.jpg  "The Dojocat"
