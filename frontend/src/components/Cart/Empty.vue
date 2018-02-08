<template>
<div class="empty">
  <h2 class="empty-message">
    Your cart is empty
  </h2>
  <button class="btn btn-primary" @click="$router.push('/')">Back to Shop</button>
</div>
</template>

<script>
export default {
  name: 'empty'
}
</script>

<style lang="scss">
$empty-background: #eee;
.empty {
  width: 80%;
  height: 60%;
  background-color: $empty-background;
  display: flex;
  flex-direction: column;
  justify-content: space-around;
  align-items: center;
}
</style>
