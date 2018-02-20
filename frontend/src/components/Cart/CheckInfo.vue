<template>
<div class="check-info">
  <div class="steptwo check-form" v-if="step===2">
    <div class="form-group">
      <label>取貨地點</label>
      <multiselect v-model="selectedStore" :options="storeList" label="label" :searchable="false" :allow-empty="false" :show-labels="false"></multiselect>
    </div>
    <div class="form-group">
      <label>付款方式</label>
      <button class="btn" :class="buttonType" v-for="method in methodList" @click="checkMethod(method)">{{ method.label }}</button>
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
import { requestStore, requestMethod } from '@/api/api'
export default {
  name: 'check-info',
  data () {
    return {
      selectedMethod: null,
      selectedStore: null,
      storeList: [],
      methodList: [],
      buttonType: 'btn-outline-secondary',
      disabled: true
    }
  },
  computed: {
    ...mapGetters({
      step: 'getStep',
      checkInfo: 'getCheck',
      cartProducts: 'getCartProducts'
    })
  },
  watch: {
    selectedMethod () {
      if (this.selectedMethod !== null && this.selectedStore !== null) {
        this.disabled = false
      }
    },
    selectedStore () {
      if (this.selectedMethod !== null && this.selectedStore !== null) {
        this.disabled = false
      }
    }
  },
  methods: {
    ...mapActions(['addStep', 'updateCheck']),
    checkMethod (method) {
      switch (method.value) {
        case 'wechat':
          this.buttonType = 'btn-outline-success'
          this.selectedMethod = method
          break
      }
    },
    updateCheckInfo () {
      console.log(this.cartProducts)
      // let params = { methodId: this.selectedMethod.id, storeId: this.selectedStore.id, statusId: 0 }
      let data = { method: this.selectedMethod, store: this.selectedStore }
      this.updateCheck(data)
      this.addStep()
    },
    getStoreList () {
      requestStore.List().then(data => {
        this.storeList = data
      }).catch(error => {
        console.log(error)
      })
    },
    getMethodList () {
      requestMethod.List().then(data => {
        this.methodList = data
      }).catch(error => {
        console.log(error)
      })
    }
  },
  created () {
    this.getStoreList()
    this.getMethodList()
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
