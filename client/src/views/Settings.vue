<template>
  <b-row>
    <b-col md="12">
      <b-card>
        <el-form :model="dynamicValidateForm" ref="dynamicValidateForm" label-width="100px" class="demo-dynamic">
          <el-form-item
            prop="email"
            label="服务器地址"
            :rules="[
              { required: true, message: '请输入邮箱地址', trigger: 'blur' },
              { type: 'ip', message: '请输入正确的邮箱地址', trigger: 'blur,change' }
            ]"
          >
            <el-input v-model="dynamicValidateForm.email"></el-input>
          </el-form-item>
          <el-form-item
            v-for="(domain, index) in dynamicValidateForm.domains"
            :label="'数据库' + index"
            :key="domain.key"
            :prop="'domains.' + index + '.value'"
            :rules="{
              required: true, message: '地址不能为空', trigger: 'blur'
            }"
          >
            <el-input v-model="domain.value"></el-input><el-button @click.prevent="removeDomain(domain)">删除</el-button>
          </el-form-item>
          <el-form-item>
            <el-button type="primary" @click="submitForm('dynamicValidateForm')">提交</el-button>
            <el-button @click="addDomain">新增</el-button>
            <el-button @click="resetForm('dynamicValidateForm')">重置</el-button>
          </el-form-item>
        </el-form>
      </b-card>
    </b-col>
  </b-row>
</template>

<script>
export default {
  data () {
    return {
      dynamicValidateForm: {
        domains: [{
          value: ''
        }],
        email: ''
      }
    }
  },
  methods: {
    submitForm (formName) {
      this.$refs[formName].validate((valid) => {
        if (valid) {
          alert('submit!')
        } else {
          console.log('error submit!!')
          return false
        }
      })
    },
    resetForm (formName) {
      this.$refs[formName].resetFields()
    },
    removeDomain (item) {
      var index = this.dynamicValidateForm.domains.indexOf(item)
      if (index !== -1) {
        this.dynamicValidateForm.domains.splice(index, 1)
      }
    },
    addDomain () {
      this.dynamicValidateForm.domains.push({
        value: '',
        key: Date.now()
      })
    }
  }
}
</script>
