<template>
<div class="finish">
  <div class="finish-title">
    <h2>結帳明細</h2>
  </div>
  <div class="status-title">
    <h4>交易狀態</h4>
  </div>
  <check-status></check-status>
  <shop-list></shop-list>
  <div class="check-title">
    <h4>付款明細</h4>
  </div>
  <check-info></check-info>
</div>
</template>

<script>
import ShopList from './ShopList'
import CheckStatus from './CheckStatus'
import CheckInfo from './CheckInfo'
export default {
  name: 'finish',
  components: {
    ShopList,
    CheckStatus,
    CheckInfo
  }
}
</script>

<style lang="scss">
.finish {
  width: 80%;
  border: 1px solid #eee;
  padding: 10px;

  .finish-title,
  .status-title,
  .check-title {
    display: flex;
  }

}
</style>
