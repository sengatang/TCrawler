<template>
  <div class="animated fadeIn">
    <b-card :header="caption" >
      <div slot="header">
        Slave主机列表
        <el-button icon="el-icon-edit" class="float-right" size="mini" @click="dialogFormVisible = true">新增主机</el-button>
        <el-dialog title="新增主机" :visible.sync="dialogFormVisible">
          <el-form :model="slaveForm" :rules="rules">
            <el-form-item label="名称" :label-width="formLabelWidth" prop="name">
              <el-input v-model="slaveForm.name" auto-complete="off"></el-input>
            </el-form-item>
            <el-form-item label="IP地址" :label-width="formLabelWidth" prop="ip">
              <el-input v-model="slaveForm.ip" auto-complete="off"></el-input>
            </el-form-item>
            <el-form-item label="端口" :label-width="formLabelWidth" prop="port">
              <el-input v-model="slaveForm.port" auto-complete="off"></el-input>
            </el-form-item>
            <el-form-item label="是否需要认证" :label-width="formLabelWidth" prop="auth">
              <el-switch v-model="slaveForm.auth"></el-switch>
            </el-form-item>
            <el-form-item label="用户名" :label-width="formLabelWidth" v-if="slaveForm.auth">
              <el-input v-model="slaveForm.username" :placeholder="请输入用户名"></el-input>
            </el-form-item>
            <el-form-item label="密码" :label-width="formLabelWidth" v-if="slaveForm.auth">
              <el-input v-model="slaveForm.password" type="password"></el-input>
            </el-form-item>
          </el-form>
          <div slot="footer" class="dialog-footer">
            <el-button @click="dialogFormVisible = false">取 消</el-button>
            <el-button type="primary" @click="addHost">确 定</el-button>
          </div>
        </el-dialog>
      </div>
      <el-table
        :data="tableData"
        style="width: 100%">
        <el-table-column
          type="selection"
          width="55">
        </el-table-column>
        <el-table-column
          prop="status"
          label="状态"
          width="100"
          :filters="[{ text: 'error', value: 0 }, { text: 'success', value: 1 }]"
          :filter-method="filterTag"
          filter-placement="bottom-end">
          <template slot-scope="scope">
            <el-tag
              :type="scope.row.status === 0 ? 'danger' : 1"
              close-transition>{{scope.row.status}}</el-tag>
          </template>
        </el-table-column>
        <el-table-column
          type="index"
          width="50">
        </el-table-column>
        <el-table-column
          prop="name"
          label="标签"
          width="180">
        </el-table-column>
        <el-table-column
          prop="ip"
          label="IP">
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
              @click="handleEdit(scope.$index, scope.row)">编辑</el-button>
            <el-button
              size="mini"
              type="danger"
              @click="deleterow(scope.$index, scope.row)">删除</el-button>
          </template>
        </el-table-column>
      </el-table>
      <el-dialog title="修改主机" :visible.sync="dialogFormVisible2">
        <el-form :model="changeForm" :rules="rules">
          <el-form-item label="名称" :label-width="formLabelWidth" prop="name">
            <el-input v-model="changeForm.name" auto-complete="off"></el-input>
          </el-form-item>
          <el-form-item label="IP地址" :label-width="formLabelWidth" prop="ip">
            <el-input v-model="changeForm.ip" auto-complete="off"></el-input>
          </el-form-item>
          <el-form-item label="端口" :label-width="formLabelWidth" prop="port">
            <el-input v-model="changeForm.port" auto-complete="off"></el-input>
          </el-form-item>
          <el-form-item label="用户名" :label-width="formLabelWidth">
            <el-input v-model="changeForm.username" :placeholder="请输入用户名"></el-input>
          </el-form-item>
          <el-form-item label="密码" :label-width="formLabelWidth">
            <el-input v-model="changeForm.password" type="password"></el-input>
          </el-form-item>
        </el-form>
        <div slot="footer" class="dialog-footer">
          <el-button @click="dialogFormVisible2 = false">取 消</el-button>
          <el-button type="primary" @click="changeHost">确 定</el-button>
        </div>
      </el-dialog>
    </b-card>
  </div>
  
  <!-- <b-row>
    <b-col md="12">
      <b-card>
        <div slot="header">
            <strong>slave主机设置</strong>
        </div>
        <el-form ref="form" :model="form" label-width="110px">
          <el-form-item label="是否保护线程">
            <el-radio-group v-model="form.process">
              <el-radio label="是"></el-radio>
              <el-radio label="否"></el-radio>
            </el-radio-group>
          </el-form-item>
          <el-form-item label="pid存储路径">
            <el-input v-model="form.address" placeholder="/var/run/redis.pid"></el-input>
          </el-form-item>
          <el-form-item label="监听端口">
            <el-input v-model="form.port" placeholder="请指定Redis监听端口..."></el-input>
          </el-form-item>
          <el-form-item label="主机地址">
            <el-input v-model="form.ip" placeholder="请输入绑定的主机地址..."></el-input>
          </el-form-item>
          <el-form-item label="timeout">
            <el-input v-model="form.timeout" placeholder="客户端闲置多长时间后关闭连接,设为0以关闭此功能..."></el-input>
          </el-form-item>
          <el-form-item label="日志记录级别">
            <el-radio-group v-model="form.log">
              <el-radio label="debug"></el-radio>
              <el-radio label="verbose"></el-radio>
              <el-radio label="notice"></el-radio>
              <el-radio label="warning"></el-radio>
            </el-radio-group>
          </el-form-item>
          <el-form-item label="数据库的数量">
            <el-input-number v-model="form.num1" @change="handleChange" :min="0" label="描述文字"></el-input-number>
          </el-form-item>
          <el-form-item label="时间/更新次数">
            <el-col :span="11">
               <el-input v-model="form.refresh" placeholder="时间间隔，以秒为单位"></el-input>
            </el-col>
            <center><el-col :span="1"> - </el-col></center>
            <el-col :span="11">
              <el-input v-model="form.refreshtimes" placeholder="更新次数"></el-input>
            </el-col>
          </el-form-item>
          <el-form-item label="是否压缩数据">
            <el-radio-group v-model="form.zip">
              <el-radio label="是"></el-radio>
              <el-radio label="否"></el-radio>
            </el-radio-group>
          </el-form-item>
          <el-form-item label="本地数据库路径">
            <el-col :span="16">
              <el-input v-model="form.local" placeholder=" ./..."></el-input>
            </el-col>
            <el-col :span="8">
              <el-input v-model="form.filename" placeholder="文件名..."></el-input>
            </el-col>
          </el-form-item>
          <el-collapse v-model="activeNames" @change="handleChange">  
            <el-collapse-item title="高级" name="1" align = "center">
              <div align = "left">与现实生活一致：与现实生活的流程、逻辑保持一致，遵循用户习惯的语言和概念；</div>
              <div>在界面中一致：所有的元素和结构需保持一致，比如：设计样式、图标和文本、元素的位置等。</div>
            </el-collapse-item>
          </el-collapse>
          <el-form-item></el-form-item>
          <el-form-item>
            <el-button type="primary" @click="onSubmit">提交修改</el-button>
            <el-button>恢复默认设置</el-button>
          </el-form-item>
        </el-form>
      </b-card>
    </b-col>
  </b-row> -->
</template>

<script>
  export default {
    data () {
      return {
        tableData: [],
        dialogFormVisible: false,
        dialogFormVisible2: false,
        changeForm: {},
        slaveForm: {
          name: '',
          ip: '',
          port: ''
        },
        formLabelWidth: '100px',
        rules: {
          name: [
            { required: true, message: '请输入主机名称', trigger: 'blur' }
          ],
          ip: [
            { required: true, message: '请输入主机IP地址', trigger: 'blur' }
          ],
          port: [
            { required: true, message: '请输入主机端口', trigger: 'blur' }
          ]
        }
      }
    },
    mounted () {
      this.fetch()
    },
    methods: {
      fetch () {
        this.$http.get('http://localhost:8000/host/list/').then(response => {
          console.log(response.body)
          this.tableData = response.body
        })
      },
      formatter (row, column) {
        return row.address
      },
      filterTag (value, row) {
        return row.status === value
      },
      filterHandler (value, row, column) {
        const property = column['property']
        return row[property] === value
      },
      deleterow (index, row) {
        this.$confirm('此操作将永久删除该主机, 是否继续?', '提示', {
          confirmButtonText: '确定',
          cancelButtonText: '取消',
          type: 'warning'
        }).then(() => {
          this.$http.delete('http://localhost:8000/host/list/' + this.tableData[index].uuid + '/').then(response => {
            this.$message({
              type: 'success',
              message: '删除成功!'
            })
            console.log(index, row)
          }, response => {
            this.$message({
              type: 'danger',
              message: '删除失败'
            })
          })
        }).catch(() => {
          this.$message({
            type: 'info',
            message: '已取消删除'
          })
        })
        this.fetch()
        // setTimeout(location.reload(), 5000)
      },
      handleEdit (index, row) {
        this.dialogFormVisible2 = true
        // console.log(this.tableData[index])
        this.changeForm = this.tableData[index]
      },
      addHost () {
        this.dialogFormVisible = false
        if (this.slaveForm.auth) { // 带验证的主机
          this.$http.post('http://localhost:8000/host/list/', {
            name: this.slaveForm.name,
            ip: this.slaveForm.ip,
            port: this.slaveForm.port,
            username: this.slaveForm.username,
            password: this.slaveForm.password
          }).then(response => {
            this.$message({
              type: 'success',
              message: '成功添加'
            })
            // # // setTimeout(location.reload(), 5000)
          }, response => {
            this.$message({
              type: 'danger',
              message: '添加失败'
            })
          })
        } else {
          this.$http.post('http://localhost:8000/host/list/', {
            name: this.slaveForm.name,
            ip: this.slaveForm.ip,
            port: this.slaveForm.port
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
        // setTimeout(location.reload(), 5000)
      },
      changeHost () {
        this.$http.patch('http://localhost:8000/host/list/' + this.changeForm.uuid + '/', {
          name: this.changeForm.name,
          ip: this.changeForm.ip,
          port: this.changeForm.port,
          username: this.changeForm.username,
          password: this.changeForm.password
        }).then(response => {
          this.dialogFormVisible2 = false
          this.$message({
            type: 'success',
            message: '成功修改'
          })
        }, response => {
          this.$message({
            type: 'danger',
            message: '修改失败'
          })
        })
        this.fetch()
        // setTimeout(location.reload(), 5000)
      }
    }
  }
</script>
    
      