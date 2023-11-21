<template>
  <div id="vditor"></div>
</template>
<script setup>
import { defineProps, ref, onMounted } from "vue";
import Vditor from "vditor";
import "vditor/dist/index.css";
const contentEditor = ref("");

onMounted(() => {
  contentEditor.value = new Vditor("vditor", {
    height: 360,
    toolbarConfig: {
      pin: true,
    },
    theme: "classic",
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

