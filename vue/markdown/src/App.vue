<template>
  <div id="app">
    <Tiptap/>
  </div>
</template>

<script>
import Tiptap from "@/components/Tiptap.vue";

export default {
  name: 'App',
  components: {
    Tiptap
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
