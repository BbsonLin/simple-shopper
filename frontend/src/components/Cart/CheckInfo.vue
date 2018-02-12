<template>
<div class="check-info">
  <div class="steptwo check-form" v-if="step===2">
    <div class="form-group">
      <label>取貨地點</label>
      <multiselect v-model="selectedStore" :options="stores" label="label" :searchable="false" :allow-empty="false" :show-labels="false"></multiselect>
    </div>
    <div class="form-group">
      <label>付款方式</label>
      <button class="btn" :class="buttonType" @click="checkMethod('wechat')">微信支付</button>
    </div>
    <div class="summary">
      <button class="btn btn-primary" :disabled="disabled" @click="updateCheckInfo">完成</button>
    </div>
  </div>
  <div class="stepthree check-form" v-if="step===3">
    <div class="form-group">
      <h5>取貨地點：</h5>
      <h6>{{ checkInfo.store.label }}</h6>
    </div>
    <div class="form-group">
      <h5>付款方式：</h5>
      <h6>{{ checkInfo.method.label }}</h6>
    </div>
  </div>
</div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'
export default {
  name: 'check-info',
  data () {
    return {
      selectedMethod: { value: 0, label: 'wechat' },
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
  computed: {
    ...mapGetters({
      step: 'getStep',
      checkInfo: 'getCheck'
    })
  },
  methods: {
    ...mapActions(['addStep', 'updateCheck']),
    checkMethod (type) {
      switch (type) {
        case 'wechat':
          this.buttonType = 'btn-outline-success'
          this.disabled = false
          break
      }
    },
    updateCheckInfo () {
      let data = { method: this.selectedMethod, store: this.selectedStore }
      this.updateCheck(data)
      this.addStep()
    }
  }
}
</script>

<style lang="scss">
.check-form {
  display: flex;
  flex-direction: column;
  width: 100%;

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

.stepthree {
  padding: 10px;

  h5,
  h6 {
    margin: auto 0;
  }
}

</style>
