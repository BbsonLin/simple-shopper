const state = {
  products: []
}

const getters = {
  getProducts: (state) => {
    return state.products
  }
}

const actions = {
  updateCart ({ commit }, data) {
    commit('UPDATE_CART', data)
  }
}

const mutations = {
  UPDATE_CART (state, data) {
    state.products.push(data)
  }
}

export default {
  state,
  getters,
  actions,
  mutations
}
