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
          width="180">
          <template slot-scope="scope">
            <i class="el-icon-time"></i>
            <span style="margin-left: 10px">{{ scope.row.date }}</span>
          </template>
        </el-table-column>
        <el-table-column
          prop="tag"
          label="类型"
          width="100">
        </el-table-column>
        <el-table-column
          prop="name"
          label="数据库名称"
          width="180">
        </el-table-column>
        <el-table-column
          prop="address"
          label="地址"
          :formatter="formatter">
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
              @click="stopconfirm">停用此设置</el-button>
              <!-- handleEdit(scope.$index, scope.row) -->
          </template>
        </el-table-column>
      </el-table>
    </b-card>
    <b-card class="card-accent-secondary" header="Card with accent">
      <div slot="header">
        曾使用的数据库设置
        <b-badge variant="secondary" class="float-right">Previous</b-badge>
      </div>
      <el-table
        :data="tableData"
        style="width: 100%">
        <el-table-column
          label="日期"
          width="180">
          <template slot-scope="scope">
            <i class="el-icon-time"></i>
            <span style="margin-left: 10px">{{ scope.row.date }}</span>
          </template>
        </el-table-column>
        <el-table-column
          prop="tag"
          label="类型"
          width="100"
          :filters="[{ text: 'MySQL', value: 'MySQL' }, { text: 'MongoDB', value: 'MongoDB' }]"
          :filter-method="filterTag"
          filter-placement="bottom-end">
          <template slot-scope="scope">
            <el-tag
              :type="scope.row.tag === 'MySQL' ? 'primary' : 'success'"
              close-transition>{{scope.row.tag}}</el-tag>
          </template>
        </el-table-column>
        <el-table-column
          prop="name"
          label="数据库名称"
          width="180">
        </el-table-column>
        <el-table-column
          prop="address"
          label="地址"
          :formatter="formatter">
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
              @click="dialogFormVisible = true">重新启用</el-button>
              <!-- handleEdit(scope.$index, scope.row) -->
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
          </template>
        </el-table-column>
      </el-table>
    </b-card>
  </div>
</template>

<script>
  export default {
    data () {
      return {
        tableNow: [{
          date: '2016-05-02',
          name: 'Test',
          address: '10.9.27.19',
          tag: 'MySQL',
          port: 200
        }],
        tableData: [{
          date: '2016-05-02',
          name: 'Test',
          address: '10.9.27.19',
          tag: 'MySQL',
          port: 200
        }, {
          date: '2016-05-04',
          name: 'Local',
          address: '127.0.0.3',
          tag: 'MySQL',
          port: 8080
        }, {
          date: '2016-05-01',
          name: 'What',
          address: '120.110.120.1',
          tag: 'MongoDB',
          port: 1080
        }, {
          date: '2016-05-03',
          name: 'None',
          address: '100.100.02.22',
          tag: 'MongoDB',
          port: 200
        }],
        dialogFormVisible: false,
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
      stopconfirm () {
        this.$confirm('此操作将停用数据库并暂停所有任务, 是否继续?', '提示', {
          confirmButtonText: '确定',
          cancelButtonText: '取消',
          type: 'warning'
        }).then(() => {
          this.$message({
            type: 'success',
            message: '成功停用!'
          })
        }).catch(() => {
          this.$message({
            type: 'info',
            message: '已取消！'
          })
        })
      }
    }
  }
</script>