<template>
<div class="check">
  <div class="form-group">
    <label>取貨地點</label>
    <multiselect id="storeSelect" v-model="selectedStore" :options="stores" label="label" :searchable="false" :allow-empty="false" :show-labels="false"></multiselect>
  </div>
  <div class="form-group">
    <label>付款方式</label>
    <button class="btn" :class="buttonType" @click="checkMethod('wechat')">微信支付</button>
  </div>
  <div class="summary">
    <button class="btn btn-primary" :disabled="disabled" @click="addStep">完成</button>
  </div>
</div>
</template>

<script>
import { mapActions } from 'vuex'
export default {
  name: 'check',
  data () {
    return {
      selectedStore: { value: 0, label: '北京' },
      stores: [
        {
          value: 0,
          label: '北京'
        },
        {
          value: 1,
          label: '上海'
        }
      ],
      buttonType: 'btn-outline-secondary',
      disabled: true
    }
  },
  methods: {
    ...mapActions(['addStep']),
    checkMethod (type) {
      switch (type) {
        case 'wechat':
          this.buttonType = 'btn-outline-success'
          this.disabled = false
          break
      }
    }
  }
}
</script>

<style lang="scss">
.check {
  display: flex;
  flex-direction: column;

  .form-group {
    display: inline-flex;
    width: 30%;

    label {
      width: 100px;
      margin: auto 0;
    }

    .multiselect {
      width: calc(100% - 100px);
    }
  }

  .summary {
    display: flex;
    justify-content: flex-end;
  }
}
</style>
