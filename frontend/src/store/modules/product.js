const state = {
  activeCategories: {},
  categories: [
    {'id': 1, 'name': '分類一', 'url': '/cat1'},
    {'id': 2, 'name': '分類二', 'url': '/cat2'}
  ],
  products: [
    {'id': 1, 'image': 'https://images.unsplash.com/photo-1453831362806-3d5577f014a4', 'name': '商品一', 'description': '一個不錯的商品'},
    {'id': 2, 'image': 'https://images.unsplash.com/photo-1473093226795-af9932fe5856', 'name': '商品二', 'description': '另一個不錯的商品'},
    {'id': 3, 'image': '', 'name': '商品一', 'description': 'Lorem ipsum dolor sit, amet consectetur adipisicing elit. Tempora quam quia facilis dolor aliquid veritatis.'},
    {'id': 4, 'image': 'https://images.unsplash.com/photo-1453831362806-3d5577f014a4', 'name': '商品二', 'description': '另一個不錯的商品'},
    {'id': 5, 'image': 'https://images.unsplash.com/photo-1473093226795-af9932fe5856', 'name': '商品一', 'description': 'Lorem ipsum dolor sit, amet consectetur adipisicing elit. Tempora quam quia facilis dolor aliquid veritatis.'}
  ]
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
  }
}

const mutations = {
  UPDATE_ACTIVE_CATEGORIES (state, cat) {
    console.log('UPDATE_ACTIVE_CATEGORIES', cat)
    state.activeCategories = cat
  }
}

export default {
  state,
  getters,
  actions,
  mutations
}
