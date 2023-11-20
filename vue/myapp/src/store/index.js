import {createStore} from "vuex";

export default createStore({
    // 存放应用级别的状态
    state: {
        // 这里可以定义应用的状态属性
        name: "电热水器",
        price: 1990
    },
    // 用于从store中的state中派生一些状态
    getters: {
        // 这里可以定义派生状态的方法

    },
    // 用于同步地修改状态
    mutations: {
        // 这里可以定义修改状态的方法，通常是同步的

    },
    // 用于包含异步操作的方法，可以包含多个mutations
    actions: {
        // 这里可以定义包含异步操作的方法，通常是异步的

    },
    // 将store拆分成模块，每个模块有自己的state、getters、mutations、actions
    modules: {
        // 这里可以定义store的模块，每个模块独立管理自己的状态和操作

    }
});
