<template>
<div class="finish">
  <div class="finish-title">
    <h2>結帳明細</h2>
  </div>
  <div class="check-status">
    <h4>交易狀態</h4>
  </div>
  <shop-list></shop-list>
  <div class="check-title">
    <h4>付款明細</h4>
  </div>
  <check></check>
</div>
</template>

<script>
import ShopList from './ShopList'
import Check from './Check'
export default {
  name: 'finish',
  components: {
    ShopList,
    Check
  }
}
</script>

<style lang="scss">
.finish {
  width: 80%;
  border: 1px solid #eee;
  padding: 10px;

  .finish-title,
  .check-status,
  .check-title {
    display: flex;
  }

}
</style>
