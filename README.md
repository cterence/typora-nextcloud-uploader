# typora-nextcloud-uploader

Uploads local images included in a [Typora](https://typora.io/) markdown document into a Nextcloud instance and generates a sharing link

It allows you to visualize the images included in your markdown documents from any device

## Installation

- Install dependencies

```
pip install -r requirements.txt
```

- Set your environment variables

- In Typora, Go to Files -> Preferences -> Image
  - Set When Insert... to Upload image
  - Set Image Upload Setting to Custom Command
  - put `python3 <path/to/script>` as your command
