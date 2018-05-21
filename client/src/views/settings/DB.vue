<template>
  <div class="animated fadeIn">
    <b-card class="card-accent-primary" header="Card with accent">
      <div slot="header">
        当前正在使用的数据库存储
        <b-badge variant="primary" class="float-right">Ongoing</b-badge>
      </div>
      <el-table
        :data="tableNow"
        style="width: 100%">
        <el-table-column
          label="日期"
          width="180"
          prop="created_at">
          <template slot-scope="scope">
            <i class="el-icon-time"></i>
            <span style="margin-left: 10px">{{ scope.row.created_at }}</span>
          </template>
        </el-table-column>
        <el-table-column
          prop="dbtype"
          label="类型"
          width="100">
        </el-table-column>
        <el-table-column
          prop="name"
          label="数据库名称"
          width="180">
        </el-table-column>
        <el-table-column
          prop="ip"
          label="地址">
        </el-table-column>
        <el-table-column
          prop="port"
          label="端口"
          width="180">
        </el-table-column>
        <el-table-column label="操作">
          <template slot-scope="scope">
            <el-button
              size="mini"
              type="danger"
              @click="stopconfirm(scope.$index)">停用此设置</el-button>
              <!-- handleEdit(scope.$index, scope.row) -->
          </template>
        </el-table-column>
      </el-table>
    </b-card>
    <b-card class="card-accent-secondary" header="Card with accent">
      <div slot="header">
        其他数据库设置
        <el-button icon="el-icon-edit" class="float-right" size="mini" @click="adddbVisible = true">新增数据库设置</el-button>
      </div>
      <el-dialog title="新增数据库设置" :visible.sync="adddbVisible">
        <el-form :model="dbForm" :rules="rules">
          <el-form-item label="名称" :label-width="formLabelWidth" prop="name">
            <el-input v-model="dbForm.name" auto-complete="off"></el-input>
          </el-form-item>
          <el-form-item label="数据库类型" :label-width="formLabelWidth" prop="dbtype">
            <el-input v-model="dbForm.dbtype" auto-complete="off"></el-input>
          </el-form-item>
          <el-form-item label="IP地址" :label-width="formLabelWidth" prop="ip">
            <el-input v-model="dbForm.ip" auto-complete="off"></el-input>
          </el-form-item>
          <el-form-item label="端口" :label-width="formLabelWidth" prop="port">
            <el-input v-model="dbForm.port" auto-complete="off"></el-input>
          </el-form-item>
          <el-form-item label="是否需要认证" :label-width="formLabelWidth" prop="auth">
            <el-switch v-model="dbForm.auth"></el-switch>
          </el-form-item>
          <el-form-item label="用户名" :label-width="formLabelWidth" v-if="dbForm.auth">
            <el-input v-model="dbForm.username" :placeholder="请输入用户名"></el-input>
          </el-form-item>
          <el-form-item label="密码" :label-width="formLabelWidth" v-if="dbForm.auth">
            <el-input v-model="dbForm.password" type="password"></el-input>
          </el-form-item>
        </el-form>
        <div slot="footer" class="dialog-footer">
          <el-button @click="adddbVisible = false">取 消</el-button>
          <el-button type="primary" @click="adddb">确 定</el-button>
        </div>
      </el-dialog>
      <el-table
        :data="tableData"
        style="width: 100%">
        <el-table-column
          label="日期"
          width="180"
          prop="created_at">
          <template slot-scope="scope">
            <i class="el-icon-time"></i>
            <span style="margin-left: 10px">{{ scope.row.created_at }}</span>
          </template>
        </el-table-column>
        <el-table-column
          prop="dbtype"
          label="类型"
          width="100">
        </el-table-column>
        <el-table-column
          prop="name"
          label="数据库名称"
          width="180">
        </el-table-column>
        <el-table-column
          prop="ip"
          label="地址">
        </el-table-column>
        <el-table-column
          prop="port"
          label="端口"
          width="180">
        </el-table-column>
        <el-table-column label="操作">
          <template slot-scope="scope">
            <el-button
              size="mini"
              @click="putinuse(scope.$index, scope.row)">启用</el-button>
              <!-- handleEdit(scope.$index, scope.row) -->
              <el-button
              size="mini"
              type="danger"
              @click="deletedb(scope.$index, scope.row)">删除</el-button>
          </template>
        </el-table-column>
      </el-table>
      <el-dialog title="数据库验证" :visible.sync="dialogFormVisible">
        <el-form :model="form">
          <el-form-item label="用户名" :label-width="formLabelWidth">
            <el-input v-model="form.username" :placeholder="请输入用户名"></el-input>
          </el-form-item>
          <el-form-item label="密码" :label-width="formLabelWidth">
            <el-input v-model="form.password" type="password"></el-input>
          </el-form-item>
        </el-form>
        <div slot="footer" class="dialog-footer">
          <el-button @click="dialogFormVisible = false">取 消</el-button>
          <el-button type="primary" @click="dialogFormVisible = false">确 定</el-button>
        </div>
      </el-dialog>
    </b-card>
  </div>
</template>

<script>
  export default {
    mounted () {
      this.fetch()
    },
    data () {
      return {
        tableNow: [],
        tableData: [],
        dialogFormVisible: false,
        adddbVisible: false,
        dbForm: {},
        form: {
          name: '',
          region: '',
          date1: '',
          date2: '',
          delivery: false,
          type: [],
          resource: '',
          desc: ''
        },
        formLabelWidth: '80px'
      }
    },
    methods: {
      fetch () {
        this.$http.get('http://localhost:8000/dbconfig/current/').then(response => {
          console.log(response.body)
          this.tableNow = response.body
        })
        this.$http.get('http://localhost:8000/dbconfig/list/').then(response => {
          console.log(response.body)
          this.tableData = response.body
        })
      },
      handleEdit (index, row) {
        console.log(index, row)
      },
      handleDelete (index, row) {
        console.log(index, row)
      },
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
      stopconfirm (index) {
        this.$confirm('此操作将停用数据库并暂停所有任务, 是否继续?', '提示', {
          confirmButtonText: '确定',
          cancelButtonText: '取消',
          type: 'warning'
        }).then(() => {
          this.$http.patch('http://localhost:8000/dbconfig/list/' + this.tableNow[index].uuid + '/', {
            status: 0
          }).then(response => {
            this.$message({
              type: 'success',
              message: '成功停用'
            })
            this.fetch()
          }, response => {
            this.$message({
              type: 'danger',
              message: '停用失败'
            })
          })
        }).catch(() => {
          this.$message({
            type: 'info',
            message: '已取消！'
          })
        })
      },
      adddb () {
        this.adddbVisible = false
        if (this.dbForm.auth) { // 带验证的主机
          this.$http.post('http://localhost:8000/dbconfig/list/', {
            dbtype: this.dbForm.dbtype,
            name: this.dbForm.name,
            ip: this.dbForm.ip,
            port: this.dbForm.port,
            username: this.dbForm.username,
            password: this.dbForm.password
          }).then(response => {
            this.$message({
              type: 'success',
              message: '成功添加'
            })
            this.fetch()
            // # // setTimeout(location.reload(), 5000)
          }, response => {
            this.$message({
              type: 'danger',
              message: '添加失败'
            })
          })
        } else {
          this.$http.post('http://localhost:8000/dbconfig/list/', {
            dbtype: this.dbForm.dbtype,
            name: this.dbForm.name,
            ip: this.dbForm.ip,
            port: this.dbForm.port
          }).then(response => {
            this.$message({
              type: 'success',
              message: '成功添加'
            })
          }, response => {
            this.$message({
              type: 'danger',
              message: '添加失败'
            })
          })
        }
        this.fetch()
        // # // setTimeout(location.reload(), 5000)
      },
      putinuse (index, row) {
        this.$http.patch('http://localhost:8000/dbconfig/list/' + this.tableData[index].uuid + '/', {
          status: 1
        }).then(response => {
          this.$message({
            type: 'success',
            message: '成功启用'
          })
          this.fetch()
        }, response => {
          this.$message({
            type: 'danger',
            message: '启用失败'
          })
        })
      },
      deletedb (index, row) {
        this.$confirm('此操作将永久删除该设置, 是否继续?', '提示', {
          confirmButtonText: '确定',
          cancelButtonText: '取消',
          type: 'warning'
        }).then(() => {
          this.$http.delete('http://localhost:8000/dbconfig/list/' + this.tableData[index].uuid + '/').then(response => {
            this.$message({
              type: 'active',
              message: '删除成功!'
            })
            this.fetch()
            // setTimeout(location.reload(), 5000)
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
      }
    }
  }
</script>