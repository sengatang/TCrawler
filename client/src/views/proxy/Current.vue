<template>
  <div class="animated fadeIn">
    <b-card :header="caption" >
      <div slot="header">
        代理列表
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
              prop="is_active"
              label="状态"
              width="100"
              :filters="[{ text: 'inactive', value:0 }, { text: 'active', value:1 }]"
              :filter-method="filterTag"
              filter-placement="bottom-end">
              <template slot-scope="scope">
                <el-tag
                  :type="scope.row.is_active === 0 ? 'danger' : 1"
                  close-transition>{{scope.row.is_active}}</el-tag>
              </template>
            </el-table-column>
            <el-table-column
              type="index"
              width="50">
            </el-table-column>
            <el-table-column
              prop="updated_at"
              label="日期"
              width="180">
            </el-table-column>
            <el-table-column
              prop="ip"
              label="IP">
            </el-table-column>
            <el-table-column
              prop="name"
              label="添加人"
              width="180">
            </el-table-column>
            <el-table-column label="操作">
              <template slot-scope="scope">
                <el-button
                  size="mini"
                  @click="handleEdit(scope.$index, scope.row)">编辑</el-button>
                <el-button
                  size="mini"
                  type="danger"
                  @click="deleterow(scope.$index, scope.row)">删除</el-button>
              </template>
            </el-table-column>
          </el-table>
          <el-dialog
            title="提示"
            :visible.sync="dialogVisible"
            width="30%"
            :before-close="handleClose">
            <div style="margin: 20px;"></div>
            <el-form :label-position="top" label-width="80px" :model="IpDetail">
              <el-form-item label="IP">
                <el-input v-model="IpDetail.ip"></el-input>
              </el-form-item>
              <el-form-item label="状态">
                <el-select v-model="IpDetail.is_active" placeholder="是否激活">
                  <el-option label="1 激活" value=1></el-option>
                  <el-option label="0 关闭" value=0></el-option>
                </el-select>
              </el-form-item>
            </el-form>
            <span slot="footer" class="dialog-footer">
              <el-button @click="dialogVisible = false">取 消</el-button>
              <el-button type="primary" @click="updateIP(IpDetail)">确 定</el-button>
            </span>
          </el-dialog>
        </b-col>
      </b-row>
    </b-card>
  </div>
</template>

<script>
  export default {
    data () {
      return {
        dialogVisible: false,
        tableData: [],
        IpDetail: [],
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
        return row.is_active === value
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
          this.$http.delete('http://localhost:8000/proxy/detail/' + this.tableData[index].uuid + '/').then(response => {
            this.$message({
              type: 'active',
              message: '删除成功!'
            })
            location.reload()
          }, response => {
            this.$message({
              type: 'danger',
              message: '删除失败!'
            })
            console.log(index, row)
          }).catch(() => {
            this.$message({
              type: 'info',
              message: '已取消删除'
            })
          })
        })
      },
      newproxy () {
        this.$prompt('请输入IP', '新增代理', {
          confirmButtonText: '确定',
          cancelButtonText: '取消'
        }).then(({ value }) => {
          this.$http.post('http://localhost:8000/proxy/list/', {
            ip: value
          }).then(response => {
            this.$message({
              type: 'success',
              message: '成功添加'
            })
            location.reload()
          }, response => {
            this.$message({
              type: 'danger',
              message: '添加失败'
            })
          })
        }).catch(() => {
          this.$message({
            type: 'info',
            message: '取消输入'
          })
        })
      },
      handleEdit (index, row) {
        this.dialogVisible = true
        this.IpDetail = this.tableData[index]
        console.log(this.IpDetail)
        console.log(row)
      },
      updateIP (formdata) {
        console.log(formdata)
        this.$http.post('http://localhost:8000/proxy/detail/', {formdata}).then(response => {
          this.$message({
            type: 'success',
            message: '更新成功'
          })
          this.dialogVisible = false
          location.reload()
        }, response => {
          this.$message({
            type: 'danger',
            message: '更新失败'
          })
        })
      }
    },
    mounted () {
      console.log(window.localStorage.token)
      this.$http.get('http://localhost:8000/proxy/list/').then(response => {
        console.log(response.body)
        this.tableData = response.body
      })
    }
  }
</script>
    
      
  

