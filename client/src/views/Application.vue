<template>
  <div class="animated fadeIn">
    <b-card :header="caption" >
      <div slot="header">
        申请列表
        <el-button icon="el-icon-edit" class="float-right" size="mini" @click="newproxy">新增代理</el-button>
      </div>
      <b-row>
        <b-col lg="12">
          <el-table
            :data="tableData"
            style="width: 100%">
            <el-table-column
              type="selection"
              width="55">
            </el-table-column>
            <el-table-column
              prop="tag"
              label="状态"
              width="100"
              :filters="[{ text: 'denied', value: 'denied' }, { text: 'approved', value: 'approved' }, { text: 'pending', value: 'pending' }]"
              :filter-method="filterTag"
              filter-placement="bottom-end">
              <template slot-scope="scope">
                <el-tag
                  :type="find_type (scope.row.tag)"
                  close-transition>{{scope.row.tag}}</el-tag>
              </template>
            </el-table-column>
            <el-table-column
              type="index"
              width="50">
            </el-table-column>
            <el-table-column
              prop="date"
              label="日期"
              width="180">
            </el-table-column>
            <el-table-column
              prop="address"
              label="摘要"
              :formatter="formatter">
            </el-table-column>
            <el-table-column
              prop="auth"
              label="添加人"
              width="180">
            </el-table-column>
            <el-table-column label="操作">
              <template slot-scope="scope">
                <el-button
                  size="mini"
                  @click="handleEdit(scope.$index, scope.row)">查看详情</el-button>
              </template>
            </el-table-column>
          </el-table>
        </b-col>
      </b-row>
    </b-card>
  </div>
</template>

<script>
  export default {
    data () {
      return {
        tableData: [{
          date: '2017-05-22',
          address: '10.9.27.19',
          tag: 'approved',
          auth: '机构公用'
        }, {
          date: '2018-03-14',
          address: '12.110.120.3',
          tag: 'denied',
          auth: '机构公用'
        }, {
          date: '2016-05-01',
          address: '127.0.0.1',
          tag: 'approved',
          auth: '机构公用'
        }, {
          date: '2017-12-03',
          address: '127.20.0.1',
          tag: 'denied',
          auth: 'User'
        }, {
          date: '2017-05-22',
          address: '10.9.27.19',
          tag: 'pending',
          auth: '机构公用'
        }],
        dialogFormVisible: false,
        form: {
          name: '',
          ip: '',
          port: ''
        },
        formLabelWidth: '100px'
      }
    },
    methods: {
      formatter (row, column) {
        return row.address
      },
      filterTag (value, row) {
        return row.tag === value
      },
      filterHandler (value, row, column) {
        const property = column['property']
        return row[property] === value
      },
      deleterow (index, row) {
        this.$confirm('此操作将永久删除该代理, 是否继续?', '提示', {
          confirmButtonText: '确定',
          cancelButtonText: '取消',
          type: 'warning'
        }).then(() => {
          this.$message({
            type: 'approved',
            message: '删除成功!'
          })
          console.log(index, row)
        }).catch(() => {
          this.$message({
            type: 'info',
            message: '已取消删除'
          })
        })
      },
      newproxy () {
        this.$prompt('请输入IP，多个IP请用逗号隔开', '新增代理', {
          confirmButtonText: '确定',
          cancelButtonText: '取消'
        }).then(({ value }) => {
          this.$message({
            type: 'success',
            message: '成功添加'
          })
        }).catch(() => {
          this.$message({
            type: 'info',
            message: '取消输入'
          })
        })
      },
      fortest () {
        console.log('test')
      },
      find_type (tag) {
        if (tag === 'denied') {
          return 'danger'
        }
        if (tag === 'pending') {
          return 'warning'
        }
        if (tag === 'approved') {
          return 'success'
        }
      }
    }
  }
</script>
    
      
  

