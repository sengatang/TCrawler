<template>
  <el-table
    :data="tableData5"
    style="width: 100%">
    <el-table-column type="expand">
      <template slot-scope="props">
        <el-form label-position="left" inline class="demo-table-expand">
          <el-form-item label="任务名称">
            <span>{{ props.row.tag }}</span>
          </el-form-item>
          <el-form-item label="任务发起人">
            <span>{{ props.row.author }}</span>
          </el-form-item>
            <el-form-item label="任务编号"
              type="index"
              width="50">
              <sapn>{{props.row.index}}</sapn>
            </el-form-item>
          <el-form-item label="爬取url">
            <span>{{ props.row.target_url}}</span>
          </el-form-item>
          <!-- <el-form-item label="系统配置">
            <template slot-scope="scope">
                <el-button
                    size="mini"
                    @click="handleEdit(scope.$index, scope.row)">导出配置文件</el-button>
            </template>
          </el-form-item> -->
          <el-form-item label="存储地址">
            <span>{{ props.row.result }}</span>
          </el-form-item>
          <el-form-item label="爬取状态">
            <span>{{ props.row.status }}</span>
          </el-form-item>
        </el-form>
      </template>
    </el-table-column>
    <el-table-column
      label="任务编号"
      prop="id">
    </el-table-column>
    <el-table-column
      label="任务名称"
      prop="tag">
    </el-table-column>
    <el-table-column
      label="任务持续时间"
      prop="last_time">
      <el-progress :percentage="20" ></el-progress>
    </el-table-column>
    <el-table-column
      label="操作"
      prop="opt">
      <template slot-scope="scope">
        <el-button
          size="mini"
          @click="handleEdit(scope.$index, scope.row)">修改任务</el-button>
        <el-button
          size="mini"
          type="danger"
          @click="handleDelete(scope.$index, scope.row)">停止任务</el-button>
      </template>
    </el-table-column>
  </el-table>
</template>

<style>
  .demo-table-expand {
    font-size: 0;
  }
  .demo-table-expand label {
    width: 90px;
    color: #99a9bf;
  }
  .demo-table-expand .el-form-item {
    margin-right: 0;
    margin-bottom: 0;
    width: 50%;
  }
</style>

<script>
  export default {
    data () {
      return {
        tableData5: []
      }
    }
    // ,
    // methods: {

    // },
    // mounted: {

    // }
}
</script>

<!--template>
  <el-table
    :data="tableData"
    border
    style="width: 100%">
    <el-table-column
      prop="name"
      label="任务名称"
      width="120">
    </el-table-column>
    <el-table-column
      fixed
      prop="date"
      label="任务持续时间"
      width="200">
    </el-table-column>
    <el-table-column
      prop="province"
      label="任务数据存储地址"
      width="300">
    </el-table-column>
    <el-table-column
      prop="city"
      label="任务系统设置"
      width="120">
      <template slot-scope="scope">
        <el-button @click="handleClick(scope.row)" type="text" size="small">查看</el-button>
      </template>
    </el-table-column>
    <el-table-column
      label="操作"
      width="200">
      <template slot-scope="scope">
        <el-button @click="handleClick(scope.row)" type="text" size="small">查看详情</el-button>
        <el-button type="text" size="small">编辑</el-button>
      </template>
    </el-table-column>
  </el-table>
</template>

<script--!>
//   export default {
//     methods: {
//       handleClick (row) {
//         console.log(row)
//       }
//     },

//     data () {
//       return {
//         tableData: [{
//           date: '2016-05-03 - 2018-03-21',
//           name: '王小虎',
//           province: '上海',
//           city: '普陀区',
//           address: '上海市普陀区金沙江路 1518 弄',
//           zip: 200333
//         }, {
//           date: '2016-05-02 - 2016-05-03',
//           name: '王小虎',
//           province: '上海',
//           city: '普陀区',
//           address: '上海市普陀区金沙江路 1518 弄',
//           zip: 200333
//         }, {
//           date: '2016-05-04 - 2016-05-02',
//           name: '王小虎',
//           province: '上海',
//           city: '普陀区',
//           address: '上海市普陀区金沙江路 1518 弄',
//           zip: 200333
//         }, {
//           date: '2016-05-01 - 2016-05-02',
//           name: '王小虎',
//           province: '上海',
//           city: '普陀区',
//           address: '上海市普陀区金沙江路 1518 弄',
//           zip: 200333
//         }]
//       }
//     }
//   }
// </script>