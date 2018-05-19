<template>
  <div class="animated fadeIn">
    <b-card :header="caption">
        <b-row>
        <b-col lg="12">
            <b-form-group>
            <label for="previous_task_search">搜索</label>
            <input v-model="search" class="form-control" placeholder="请输入任务名称搜索..." id="previous_task_search">
            </b-form-group>
            <c-table caption="<i class='fa fa-align-justify'></i> 当前任务"></c-table>
        </b-col>
        </b-row>
    </b-card>
  </div>
</template>

<script>
  import cTable from '../base/CurrentTaskTable.vue'

  export default {
    name: 'tables',
    components: {cTable},
    data: {
      sortKey: name
    },
    methods: {
      sortBy: function (sortKey) {
        this.reverse = (this.sortKey === sortKey) ? !this.reverse : false

        this.sortKey = sortKey
      },
      addUser: function () {
        this.users.push(this.newUser)
        this.newUser = {}
      }
    }
  }
</script>
