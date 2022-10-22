import uuid
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin, User


class TimestampedModel(models.Model):
    # 생성된 날짜를 기록
    created_time = models.DateTimeField(auto_now_add=True)
    # 수정된 날짜를 기록
    updated_time = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ['-created_time', '-updated_time']


class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('이메일 주소를 입력해주세요.')
        if not password:
            raise ValueError('비밀번호를 입력해주세요.')
        print(password)
        # if password != password_confirm:
        #     raise ValueError('비밀번호가 일치하지 않습니다.')

        user = self.model(
            email=self.normalize_email(email),
            **extra_fields,
        )
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email=None, password=None, **extra_fields):
        superuser = self.create_user(
            email=email,
            password=password,
            **extra_fields,
        )
        superuser.is_staff = True
        superuser.is_superuser = True
        superuser.save(using=self._db)

        return superuser


class User(AbstractBaseUser, PermissionsMixin, TimestampedModel):
    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_type = models.CharField(max_length=255, blank=True, null=True)
    nickname = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(unique=True)
    user_policy_argreement = models.BooleanField(default=False)
    is_valid = models.BooleanField(default=False)
    self_intro = models.CharField(max_length=255, blank=True, null=True)
    profile_image = models.CharField(max_length=255, blank=True, null=True)  # 이미지 파일 링크였나..?
    # desired_fee_unit = models.CharField(max_length=255, blank=True, null=True)
    # desired_fee_value = models.CharField(max_length=255, blank=True, null=True)

    USERNAME_FIELD = 'email'
    
    # REQUIRED_FIELDS = [
    #     'user_type',
    #     'nickname',
    # ]
    
    objects = UserManager()
    
    def __str__(self):
        return self.email
    
    def get_full_name(self):
        return self.nickname
    
    def get_short_name(self):
        return self.nickname

    class Meta:
        db_table = 'user'


# class Degree(models.Model):
#     degree_name = models.CharField(primary_key=True, max_length=255)
#     org_name = models.ForeignKey('Organization', models.DO_NOTHING, db_column='org_name')
#     major = models.ForeignKey('Major', models.DO_NOTHING, db_column='major')

#     class Meta:
#         managed = False
#         db_table = 'degree'
#         unique_together = (('degree_name', 'org_name', 'major'),)


# class Userdegree(models.Model):
#     user = models.OneToOneField(User, models.DO_NOTHING, primary_key=True)
#     degree_name = models.ForeignKey(Degree, models.DO_NOTHING, db_column='degree_name')
#     org_name = models.ForeignKey(Degree, models.DO_NOTHING, db_column='org_name')
#     major = models.ForeignKey(Degree, models.DO_NOTHING, db_column='major')
#     grad_status = models.CharField(max_length=255, blank=True, null=True)
#     start_time = models.CharField(max_length=255, blank=True, null=True)
#     end_time = models.CharField(max_length=255, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'userdegree'
#         unique_together = (('user', 'degree_name', 'org_name', 'major'),)


# class Expertfield(models.Model):
#     field_name = models.CharField(primary_key=True, max_length=255)

#     class Meta:
#         managed = False
#         db_table = 'expertfield'


# class Userexpertfield(models.Model):
#     user = models.OneToOneField(User, models.DO_NOTHING, primary_key=True)
#     field_name = models.ForeignKey(Expertfield, models.DO_NOTHING, db_column='field_name')

#     class Meta:
#         managed = False
#         db_table = 'userexpertfield'
#         unique_together = (('user', 'field_name'),)


# class Company(models.Model):
#     company_name = models.CharField(primary_key=True, max_length=255)

#     class Meta:
#         managed = False
#         db_table = 'company'


# class Userworkexp(models.Model):
#     position = models.CharField(primary_key=True, max_length=255)
#     user = models.ForeignKey(User, models.DO_NOTHING)
#     company_name = models.ForeignKey(Company, models.DO_NOTHING, db_column='company_name')
#     start_time = models.CharField(max_length=255, blank=True, null=True)
#     end_time = models.CharField(max_length=255, blank=True, null=True)
#     work_exp_details = models.CharField(max_length=255, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'userworkexp'
#         unique_together = (('position', 'user', 'company_name'),)


# class Companylogofile(models.Model):
#     logo_type = models.OneToOneField('Logotype', models.DO_NOTHING, db_column='logo_type', primary_key=True)
#     company_name = models.ForeignKey(Company, models.DO_NOTHING, db_column='company_name')
#     file_url = models.CharField(max_length=255, blank=True, null=True)
#     file_name = models.CharField(max_length=255, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'companylogofile'
#         unique_together = (('logo_type', 'company_name'),)


# class Degreeauthfile(models.Model):
#     degree_name = models.OneToOneField(Degree, models.DO_NOTHING, db_column='degree_name', primary_key=True)
#     org_name = models.ForeignKey(Degree, models.DO_NOTHING, db_column='org_name')
#     major = models.ForeignKey(Degree, models.DO_NOTHING, db_column='major')
#     file_url = models.CharField(max_length=255, blank=True, null=True)
#     file_name = models.CharField(max_length=255, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'degreeauthfile'
#         unique_together = (('degree_name', 'org_name', 'major'),)


# class Logotype(models.Model):
#     logo_type = models.CharField(primary_key=True, max_length=255)
#     width = models.CharField(max_length=255, blank=True, null=True)
#     height = models.CharField(max_length=255, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'logotype'


# class Major(models.Model):
#     major = models.CharField(primary_key=True, max_length=255)

#     class Meta:
#         managed = False
#         db_table = 'major'


# class Organization(models.Model):
#     org_name = models.CharField(primary_key=True, max_length=255)

#     class Meta:
#         managed = False
#         db_table = 'organization'


# class Organizationlogofile(models.Model):
#     org_name = models.OneToOneField(Organization, models.DO_NOTHING, db_column='org_name', primary_key=True)
#     logo_type = models.ForeignKey(Logotype, models.DO_NOTHING, db_column='logo_type')
#     file_url = models.CharField(max_length=255, blank=True, null=True)
#     file_name = models.CharField(max_length=255, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'organizationlogofile'
#         unique_together = (('org_name', 'logo_type'),)


# class Realserviceinfo(models.Model):
#     req = models.OneToOneField('Transrequest', models.DO_NOTHING, primary_key=True)
#     real_end_time = models.CharField(max_length=255, blank=True, null=True)
#     real_fee_unit = models.CharField(max_length=255, blank=True, null=True)
#     real_fee_value = models.CharField(max_length=255, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'realserviceinfo'


# class Servicetype(models.Model):
#     service_name = models.CharField(primary_key=True, max_length=255)

#     class Meta:
#         managed = False
#         db_table = 'servicetype'

