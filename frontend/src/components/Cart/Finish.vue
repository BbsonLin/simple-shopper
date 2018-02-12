<template>
<div class="finish">
  <div class="finish-title">
    <h2>結帳明細</h2>
  </div>
  <div class="check-status">
    <h4>交易狀態</h4>
  </div>
  <div class="check">
    <div class="form-group"></div>
    <div class="form-group"></div>
  </div>
  <shop-list></shop-list>
</div>
</template>

<script>
import ShopList from './ShopList'
export default {
  name: 'finish',
  components: {
    ShopList
  }
}
</script>

<style lang="scss">
.finish {
  width: 80%;
  border: 1px solid #eee;
  padding: 10px;

  .finish-title {
    display: flex;
  }

  .check-status {
    display: flex;
  }
}
</style>
