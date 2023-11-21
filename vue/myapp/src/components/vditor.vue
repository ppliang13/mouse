<template>
  <div id="vditor"></div>
</template>
<script setup>
import {defineProps, ref, onMounted} from "vue";
import Vditor from "vditor";
import "vditor/dist/index.css";

const contentEditor = ref("");

onMounted(() => {
  contentEditor.value = new Vditor("vditor", {
    height: 360,
    toolbarConfig: {
      pin: true,
    },
    toolbar:
        [
          "emoji",
          "headings",
          "bold",
          "italic",
          "strike",
          "link",
          "|",
          "list",
          "ordered-list",
          "check",
          "outdent",
          "indent",
          "|",
          "quote",
          "line",
          "code",
          "inline-code",
          "insert-before",
          "insert-after",
          "|",
          "upload",
          "record",
          "table",
          "|",
          "undo",
          "redo",
          "|",
          "fullscreen",
          "edit-mode",
          {
            name: "more",
            toolbar: [
              "both",
              "code-theme",
              "content-theme",
              "export",
              "outline",
              "preview",
              "devtools",
              "info",
              "help",
            ],
          },
          {
            hotkey: '⇧⌘S',
            name: 'sponsor',
            tipPosition: 's',
            tip: '大纲生成',
            className: 'right',
            icon: "<svg t=\"1700553099326\" class=\"icon\" viewBox=\"0 0 1024 1024\" version=\"1.1\" xmlns=\"http://www.w3.org/2000/svg\" p-id=\"5422\"\n" +
                "     xmlns:xlink=\"http://www.w3.org/1999/xlink\" width=\"200\" height=\"200\">\n" +
                "    <path d=\"M554.666667 251.733333V341.333333h341.333333v426.666667H170.666667V341.333333h341.333333V251.733333c-25.6-8.533333-42.666667-34.133333-42.666667-59.733333 0-34.133333 29.866667-64 64-64s64 29.866667 64 64c0 29.866667-17.066667 51.2-42.666666 59.733333zM512 384H213.333333v341.333333h640V384h-341.333333z m-384 85.333333v213.333334H85.333333v-213.333334h42.666667z m853.333333 0v213.333334h-42.666666v-213.333334h42.666666zM384 597.333333c-25.6 0-42.666667-17.066667-42.666667-42.666666s17.066667-42.666667 42.666667-42.666667 42.666667 17.066667 42.666667 42.666667-17.066667 42.666667-42.666667 42.666666z m298.666667 0c-25.6 0-42.666667-17.066667-42.666667-42.666666s17.066667-42.666667 42.666667-42.666667 42.666667 17.066667 42.666666 42.666667-17.066667 42.666667-42.666666 42.666666z\"\n" +
                "          fill=\"#444444\" p-id=\"5423\"></path>\n" +
                "</svg>",
            click () {
              //获取mark文档的内容
              console.log(contentEditor.value.getValue());
            },
          }
        ],
    counter: {
      enable: true
    },
    cache: {
      enable: false,
    },
    after: () => {
      contentEditor.value.setValue("hello,Vditor+Vue!");
    },
  });
});


</script>
<style scoped>
a {
  color: #42b983;
}

/* 左对齐文本 */
.vditor {
  text-align: left !important;
}

/* 或者更具体一些 */
#vditor {
  text-align: left !important;
}

</style>

