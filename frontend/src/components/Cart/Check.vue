<template>
<div class="check">
  <div class="form-group">
    <label for="storeSelect">取貨地點</label>
    <multiselect id="storeSelect" v-model="selectedStore" :options="stores" label="label" :searchable="false" :allow-empty="false" :show-labels="false"></multiselect>
  </div>
</div>
</template>

<script>
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
      ]
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
  }
}
</style>
