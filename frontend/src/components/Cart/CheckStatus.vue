<template>
<div class="check-status">
  <table class="table">
    <tbody>
      <tr class="table-active">
        <td>訂單編號</td>
        <td>訂購時間</td>
        <td>訂單金額</td>
        <td>訂單狀態</td>
        <td>操作</td>
      </tr>
      <tr>
        <td>{{ check.id }}</td>
        <td>{{ check.datetime }}</td>
        <td>{{ check.totalAmount }}</td>
        <td>{{ check.status }}</td>
        <td>
          <a href="javascript(0)">取消訂單</a>
        </td>
      </tr>
    </tbody>
  </table>
</div>
</template>

<script>
export default {
  name: 'check-status',
  data () {
    return {
      check: {
        id: '00001111',
        datetime: '2018-02-12 18:05',
        totalAmount: 1000,
        status: '未付款'
      }
    }
  }
}
</script>

<style lang="scss">
</style>
