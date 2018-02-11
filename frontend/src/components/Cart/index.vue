<template>
<div class="cart">
  <h1 class="cart-title">Cart</h1>
  <empty v-if="!totalNumber"></empty>
  <stepone v-if="totalNumber && step===1"></stepone>
  <div class="check-button">
    <button class="btn btn-primary" v-if="totalNumber" @click="cartEvent">{{ button.content }}</button>
  </div>
</div>
</template>

<script>
import Empty from './Empty'
import Stepone from './Stepone'
import { mapGetters } from 'vuex'
export default {
  name: 'cart',
  components: {
    Empty,
    Stepone
  },
  data () {
    return {
      step: 1,
      button: {
        content: '結帳'
      }
    }
  },
  computed: {
    ...mapGetters({
      totalNumber: 'getTotalNumber'
    })
  },
  methods: {
    cartEvent () {
      switch (this.step) {
        case 1:
          this.step++
          this.button.content = '完成'
          break
        case 2:
          this.step = 1
          this.button.content = '結帳'
          break
      }
    }
  }
}
</script>

<style lang="scss">
.cart {
  padding: 10px;
  height: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.check-button {
  width: 80%;
  display: flex;
  justify-content: flex-end;
}
</style>
