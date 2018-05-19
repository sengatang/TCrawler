<template>
   <div class="animated fadeIn">
    <b-row>
      <b-col md="12">
        <b-card header="当前活跃任务">
          <b-row>
            <b-col sm="12" lg="4">
              <b-row>
                <b-col sm="6">
                  <Callout variant="info">
                    <small class="text-muted">总爬虫数</small><br>
                    <strong class="h4">123</strong>
                    <div class="chart-wrapper">
                      <callout-chart-example :data="[35, 23, 56, 22, 97, 23, 64]" variant="#20a8d8" width="80" height="30" />
                    </div>
                  </Callout>
                </b-col>
                <b-col sm="6">
                  <Callout variant="danger">
                    <small class="text-muted">当前活跃爬虫</small><br>
                    <strong class="h4">43</strong>
                    <div class="chart-wrapper">
                      <callout-chart-example :data="[65, 59, 84, 84, 51, 55, 40]" variant="#f86c6b" width="80" height="30" />
                    </div>
                  </Callout>
                </b-col>
              </b-row>
              <hr class="mt-0">
              <ul class="horizontal-bars">
                <li>
                  <div class="title">
                    Monday
                  </div>
                  <div class="bars">
                    <b-progress height={} class="progress-xs" :value="34" variant="info"></b-progress>
                    <b-progress height={} class="progress-xs" :value="78" variant="danger"></b-progress>
                  </div>
                </li>
                <li>
                  <div class="title">
                    Tuesday
                  </div>
                  <div class="bars">
                    <b-progress height={} class="progress-xs" :value="56" variant="info"></b-progress>
                    <b-progress height={} class="progress-xs" :value="94" variant="danger"></b-progress>
                  </div>
                </li>
                <li>
                  <div class="title">
                    Wednesday
                  </div>
                  <div class="bars">
                    <b-progress height={} class="progress-xs" :value="12" variant="info"></b-progress>
                    <b-progress height={} class="progress-xs" :value="67" variant="danger"></b-progress>
                  </div>
                </li>
                <li>
                  <div class="title">
                    Thursday
                  </div>
                  <div class="bars">
                    <b-progress height={} class="progress-xs" :value="43" variant="info"></b-progress>
                    <b-progress height={} class="progress-xs" :value="91" variant="danger"></b-progress>
                  </div>
                </li>
                <li>
                  <div class="title">
                    Friday
                  </div>
                  <div class="bars">
                    <b-progress height={} class="progress-xs" :value="22" variant="info"></b-progress>
                    <b-progress height={} class="progress-xs" :value="73" variant="danger"></b-progress>
                  </div>
                </li>
                <li>
                  <div class="title">
                    Saturday
                  </div>
                  <div class="bars">
                    <b-progress height={} class="progress-xs" :value="53" variant="info"></b-progress>
                    <b-progress height={} class="progress-xs" :value="82" variant="danger"></b-progress>
                  </div>
                </li>
                <li>
                  <div class="title">
                    Sunday
                  </div>
                  <div class="bars">
                    <b-progress height={} class="progress-xs" :value="9" variant="info"></b-progress>
                    <b-progress height={} class="progress-xs" :value="69" variant="danger"></b-progress>
                  </div>
                </li>
                <li class="legend">
                  <b-badge pill variant="info"></b-badge> <small>New clients</small> &nbsp; <b-badge pill variant="danger"></b-badge> <small>Recurring clients</small>
                </li>
              </ul>
            </b-col>
            <b-col sm="6" lg="4">
              <b-row>
                <b-col sm="6">
                  <Callout variant="warning">
                    <small class="text-muted">爬取url总数</small><br>
                    <strong class="h4">78,623</strong>
                    <div class="chart-wrapper">
                      <callout-chart-example :data="[35, 23, 56, 22, 97, 23, 64]" variant="#f8cb00" width="80" height="30" />
                    </div>
                  </Callout>
                </b-col>
                <b-col sm="6">
                </b-col>
              </b-row>
              <hr class="mt-0">
            </b-col>
            <b-col sm="6" lg="4">
              <b-row>
                <b-col sm="6">
                  <Callout>
                    <small class="text-muted">爬虫使用率</small><br>
                    <strong class="h4">35%</strong>
                    <div class="chart-wrapper">
                      <callout-chart-example :data="[78, 81, 80, 45, 34, 12, 40]" width="80px" height="30" />
                    </div>
                  </Callout>
                </b-col>
                <b-col sm="6">
                  <Callout variant="primary">
                    <small class="text-muted">Bounce Rate</small><br>
                    <strong class="h4">5%</strong>
                    <div class="chart-wrapper">
                      <callout-chart-example :data="[35, 23, 56, 22, 97, 23, 64]" variant="#20a8d8" width="80px" height="30" />
                    </div>
                  </Callout>
                </b-col>
              </b-row>
              <hr class="mt-0">
            </b-col>
          </b-row>
          <br/>
          <b-table class="mb-0 table-outline" responsive="sm" hover :items="tableItems" :fields="tableFields" head-variant="light" @click="open">
            <div slot="avatar" class="avatar" slot-scope="item" >
              <img :src="item.value.url" class="img-avatar" alt="">
              <span class="avatar-status" v-bind:class="{ 'bg-success': item.value.status == 'success',  'bg-warning': item.value.status == 'warning', 'bg-danger': item.value.status == 'danger', 'bg-secondary': item.value.status == '' }"></span>
            </div>
            <div slot="user" slot-scope="item">
              <div>{{item.value.name}}</div>
              <div class="small text-muted">
                <span>
                  <template v-if="item.value.new">New</template>
                  <template v-else>Recurring</template>
                </span> | 任务开始时间: {{item.value.registered}}
              </div>
            </div>
            <i slot="country" class="h4 mb-0" :class="flag(item.value.flag)" slot-scope="item" :title="item.value.flag" :id="item.value.flag"></i>
            <i class="flag-icon flag-icon-pw h1" title="pw" id="pw"></i>
            <div slot="usage" slot-scope="item">
              <div class="clearfix">
                <div class="float-left">
                  <strong>{{item.value.value}}%</strong>
                </div>
                <div class="float-right">
                  <small class="text-muted">{{item.value.period}}</small>
                </div>
              </div>
              <b-progress height={} class="progress-xs" v-model="item.value.value" :variant="variant(item.value.value)"></b-progress>
            </div>
            <i slot="payment" slot-scope="item" :class="item.value.icon" style="font-size:24px"></i>
            <div slot="activity" slot-scope="item">
              <div class="small text-muted">Last login</div>
              <strong>{{item.value}}</strong>
            </div>
            <div slot="option">
              <template slot-scope="scope">
                <el-button
                    size="mini"
                    @click="open()">导出配置文件</el-button>
              </template>
            </div>
          </b-table>
        </b-card>
      </b-col>
    </b-row>
   </div>
</template>

<script>
export default {
  data: function () {
    return {
      selected: 'Month',
      tableItems: [
        {
          avatar: { url: 'static/img/avatars/1.jpg', status: 'success' },
          user: { name: 'Yiorgos Avraamu', new: true, registered: 'Jan 1, 2015' },
          country: { name: 'USA', flag: 'us' },
          usage: { value: 50, period: 'Jun 11, 2015 - Jul 10, 2015' },
          payment: { name: 'Mastercard', icon: 'fa fa-cc-mastercard' },
          activity: '10 sec ago'
        },
        {
          avatar: { url: 'static/img/avatars/2.jpg', status: 'danger' },
          user: { name: 'Avram Tarasios', new: false, registered: 'Jan 1, 2015' },
          country: { name: 'Brazil', flag: 'br' },
          usage: { value: 22, period: 'Jun 11, 2015 - Jul 10, 2015' },
          payment: { name: 'Visa', icon: 'fa fa-cc-visa' },
          activity: '5 minutes ago'
        },
        {
          avatar: { url: 'static/img/avatars/3.jpg', status: 'warning' },
          user: { name: 'Quintin Ed', new: true, registered: 'Jan 1, 2015' },
          country: { name: 'India', flag: 'in' },
          usage: { value: 74, period: 'Jun 11, 2015 - Jul 10, 2015' },
          payment: { name: 'Stripe', icon: 'fa fa-cc-stripe' },
          activity: '1 hour ago'
        },
        {
          avatar: { url: 'static/img/avatars/4.jpg', status: '' },
          user: { name: 'Enéas Kwadwo', new: true, registered: 'Jan 1, 2015' },
          country: { name: 'France', flag: 'fr' },
          usage: { value: 98, period: 'Jun 11, 2015 - Jul 10, 2015' },
          payment: { name: 'PayPal', icon: 'fa fa-paypal' },
          activity: 'Last month'
        },
        {
          avatar: { url: 'static/img/avatars/5.jpg', status: 'success' },
          user: { name: 'Agapetus Tadeáš', new: true, registered: 'Jan 1, 2015' },
          country: { name: 'Spain', flag: 'es' },
          usage: { value: 22, period: 'Jun 11, 2015 - Jul 10, 2015' },
          payment: { name: 'Google Wallet', icon: 'fa fa-google-wallet' },
          activity: 'Last week'
        },
        {
          avatar: { url: 'static/img/avatars/6.jpg', status: 'danger' },
          user: { name: 'Friderik Dávid', new: true, registered: 'Jan 1, 2015' },
          country: { name: 'Poland', flag: 'pl' },
          usage: { value: 43, period: 'Jun 11, 2015 - Jul 10, 2015' },
          payment: { name: 'Amex', icon: 'fa fa-cc-amex' },
          activity: 'Last week'
        }
      ],
      tableFields: {
        user: {
          label: '任务名称'
        },
        usage: {
          label: '任务进度'
        },
        activity: {
          label: '上次活跃时间'
        },
        option: {
          label: '查看详情'
        }
      }
    }
  },
  methods: {
    variant (value) {
      let $variant
      if (value <= 25) {
        $variant = 'info'
      } else if (value > 25 && value <= 50) {
        $variant = 'success'
      } else if (value > 50 && value <= 75) {
        $variant = 'warning'
      } else if (value > 75 && value <= 100) {
        $variant = 'danger'
      }
      return $variant
    },
    flag (value) {
      return 'flag-icon flag-icon-' + value
    },
    open () {
      this.$alert('这是一段内容', '标题名称', {
        confirmButtonText: '确定',
        callback: action => {
          this.$message({
            type: 'info',
            message: `action: ${action}`
          })
        }
      })
    }
  }
}
</script>