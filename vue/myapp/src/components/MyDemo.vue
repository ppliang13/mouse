<script>
export default {
  name: "MyDemo",
  data() {
    return {
      name: this.$store.state.name,
      price: this.$store.state.price,
    }
  }
}
</script>

<template>
  <div>
    <h3>商品名称:{{ name }}</h3>
    <h3>商品价格:{{ price }}</h3>
  </div>
</template>

<style scoped>

</style>