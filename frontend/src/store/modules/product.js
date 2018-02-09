import axios from 'axios'

const state = {
  activeCategories: {},
  categories: [
    {'id': 1, 'name': '分類一', 'url': '/cat1'},
    {'id': 2, 'name': '分類二', 'url': '/cat2'}
  ],
  products: []
}

const getters = {
  getActiveCategories: (state) => state.activeCategories,
  getCategories: (state) => state.categories,
  getProducts: (state) => state.products
}

const actions = {
  setActiveCategories ({ commit }, payload) {
    console.log('setActiveCategories', payload)
    commit('UPDATE_ACTIVE_CATEGORIES', payload)
    axios.get('/product', { params: { 'name': payload.name } }).then(returnData => {
      commit('UPDATE_PRODUCT_LIST', returnData)
    })
  }
}

const mutations = {
  UPDATE_ACTIVE_CATEGORIES (state, cat) {
    console.log('UPDATE_ACTIVE_CATEGORIES', cat)
    state.activeCategories = cat
  },
  UPDATE_PRODUCT_LIST (state, products) {
    console.log('UPDATE_PRODUCT_LIST', products)
    state.products = products.data
  }
}

export default {
  state,
  getters,
  actions,
  mutations
}
