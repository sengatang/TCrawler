<template>
  <b-card :header="caption">
    <b-table :hover="hover" :striped="striped" :bordered="bordered" :small="small" :fixed="fixed" responsive="sm" :items="items" :fields="fields" :current-page="currentPage" :per-page="perPage">
      <template slot="代理状态" slot-scope="data">
        <b-badge :variant="getBadge(data.item.代理状态)">{{data.item.代理状态}}</b-badge>
      </template>
      <template slot-scope="scope" slot="操作">
          <el-button
            size="mini"
            @click="handleEdit(scope.$index, scope.row)">启/禁用</el-button>
          <el-button
            size="mini"
            type="danger"
            @click="handleDelete(scope.$index, scope.row)">删除</el-button>
      </template>
    </b-table>
    <nav>
      <b-pagination :total-rows="getRowCount(items)" :per-page="perPage" v-model="currentPage" prev-text="Prev" next-text="Next" hide-goto-end-buttons/>
    </nav>
  </b-card>
</template>

<script>
  /**
   * Randomize array element order in-place.
   * Using Durstenfeld shuffle algorithm.
   */
  const shuffleArray = (array) => {
    for (let i = array.length - 1; i > 0; i--) {
      let j = Math.floor(Math.random() * (i + 1))
      let temp = array[i]
      array[i] = array[j]
      array[j] = temp
    }
    return array
  }

  export default {
    name: 'c-table',
    props: {
      caption: {
        type: String,
        default: 'Table'
      },
      hover: {
        type: Boolean,
        default: false
      },
      striped: {
        type: Boolean,
        default: false
      },
      bordered: {
        type: Boolean,
        default: false
      },
      small: {
        type: Boolean,
        default: false
      },
      fixed: {
        type: Boolean,
        default: false
      }
    },
    data: () => {
      return {
        items: shuffleArray([
          {IP地址: '192.108.93.21', 添加时间: '2012/01/01', 代理状态: 'Active'},
          {IP地址: '192.108.93.121', 添加时间: '2012/02/01', 代理状态: 'Banned'},
          {IP地址: '10.29.97.82', 添加时间: '2012/02/01', 代理状态: 'Inactive'},
          {IP地址: 'Derick Maximinus', 添加时间: '2012/03/01', 代理状态: 'Pending'},
          {IP地址: 'Friderik Dávid', 添加时间: '2012/01/21', 代理状态: 'Active'},
          {IP地址: 'Yiorgos Avraamu', 添加时间: '2012/01/01', 代理状态: 'Active'},
          {IP地址: 'Avram Tarasios', 添加时间: '2012/02/01', 代理状态: 'Banned'},
          {IP地址: 'Quintin Ed', 添加时间: '2012/02/01', 代理状态: 'Inactive'},
          {IP地址: 'Enéas Kwadwo', 添加时间: '2012/03/01', 代理状态: 'Pending'},
          {IP地址: 'Agapetus Tadeáš', 添加时间: '2012/01/21', 代理状态: 'Active'},
          {IP地址: 'Carwyn Fachtna', 添加时间: '2012/01/01', 代理状态: 'Active'},
          {IP地址: 'Nehemiah Tatius', 添加时间: '2012/02/01', 代理状态: 'Banned'},
          {IP地址: 'Ebbe Gemariah', 添加时间: '2012/02/01', 代理状态: 'Inactive'},
          {IP地址: 'Eustorgios Amulius', 添加时间: '2012/03/01', 代理状态: 'Pending'},
          {IP地址: 'Leopold Gáspár', 添加时间: '2012/01/21', 代理状态: 'Active'},
          {IP地址: 'Pompeius René', 添加时间: '2012/01/01', 代理状态: 'Active'},
          {IP地址: 'Paĉjo Jadon', 添加时间: '2012/02/01', 代理状态: 'Banned'},
          {IP地址: 'Micheal Mercurius', 添加时间: '2012/02/01', 代理状态: 'Inactive'},
          {IP地址: 'Ganesha Dubhghall', 添加时间: '2012/03/01', 代理状态: 'Pending'},
          {IP地址: 'Hiroto Šimun', 添加时间: '2012/01/21', 代理状态: 'Active'},
          {IP地址: 'Vishnu Serghei', 添加时间: '2012/01/01', 代理状态: 'Active'},
          {IP地址: 'Zbyněk Phoibos', 添加时间: '2012/02/01', 代理状态: 'Banned'},
          {IP地址: 'Einar Randall', 添加时间: '2012/02/01', 代理状态: 'Inactive'},
          {IP地址: 'Félix Troels', 添加时间: '2012/03/21', 代理状态: 'Active'},
          {IP地址: 'Aulus Agmundr', 添加时间: '2012/01/01', 代理状态: 'Pending'}
        ]),
        fields: [
          {key: 'IP地址'},
          {key: '添加时间'},
          {key: '代理状态'},
          {key: '操作'}
        ],
        currentPage: 1,
        perPage: 5,
        totalRows: 0
      }
    },
    methods: {
      getBadge (代理状态) {
        return 代理状态 === 'Active' ? 'success'
          : 代理状态 === 'Inactive' ? 'secondary'
            : 代理状态 === 'Pending' ? 'warning'
              : 代理状态 === 'Banned' ? 'danger' : 'primary'
      },
      getRowCount (items) {
        return items.length
      }
    }
  }
</script>
