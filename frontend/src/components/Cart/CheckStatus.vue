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
      <tr v-for="check in checkData.checks">
        <td>{{ formatNumber(check.id) }}</td>
        <td>{{ check.update_time }}</td>
        <td>{{ check.total }}</td>
        <td>{{ check.status.name }}</td>
        <td>
          <a href="javascript(0)">取消訂單</a>
        </td>
      </tr>
    </tbody>
  </table>
</div>
</template>

<script>
import { mapGetters } from 'vuex'
export default {
  name: 'check-status',
  data () {
    return {
    }
  },
  computed: {
    ...mapGetters({
      checkData: 'getCheck'
    })
  },
  methods: {
    formatNumber (checkNumber) {
      return String(checkNumber).padStart(10, '0')
    }
  }
}
</script>

<style lang="scss">
</style>
