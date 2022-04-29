# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Course(models.Model):
    course_id = models.CharField(db_column='course_ID', primary_key=True, max_length=8)  # Field name made lowercase.
    title = models.CharField(max_length=32, blank=True, null=True)
    dept_name = models.ForeignKey('Department', models.DO_NOTHING, db_column='dept_name', blank=True, null=True, related_name='+')
    credits = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'course'


class Department(models.Model):
    dept_name = models.CharField(primary_key=True, max_length=25)
    building = models.CharField(max_length=10, blank=True, null=True)
    budget = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'department'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Instructor(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=20, blank=True, null=True)
    dept_name = models.ForeignKey(Department, models.DO_NOTHING, db_column='dept_name', blank=True, null=True, related_name='+')
    salary = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'instructor'


class Prereq(models.Model):
    course = models.OneToOneField(Course, models.DO_NOTHING, db_column='course_ID', primary_key=True)  # Field name made lowercase.
    prereq = models.ForeignKey(Course, models.DO_NOTHING, db_column='prereq_ID', related_name='+')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'prereq'
        unique_together = (('course', 'prereq'),)


class Section(models.Model):
    course = models.OneToOneField(Course, models.DO_NOTHING, db_column='course_ID', primary_key=True)  # Field name made lowercase.
    sec_id = models.CharField(db_column='sec_ID', max_length=3)  # Field name made lowercase.
    semester = models.PositiveIntegerField()
    year = models.PositiveSmallIntegerField()
    building = models.CharField(max_length=10, blank=True, null=True)
    room = models.CharField(max_length=10, blank=True, null=True)
    capacity = models.PositiveSmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'section'
        unique_together = (('course', 'sec_id', 'semester', 'year'),)


class Student(models.Model):
    id = models.PositiveIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=32, blank=True, null=True)  # Field name made lowercase.
    dept_name = models.ForeignKey(Department, models.DO_NOTHING, db_column='dept_name', blank=True, null=True, related_name='+')
    total_credits = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'student'


class Takes(models.Model):
    dbid = models.ForeignKey(Student, models.DO_NOTHING, db_column='ID', blank=True, null=True, related_name='+')  # Field name made lowercase.
    course = models.ForeignKey(Section, models.DO_NOTHING, db_column='course_ID', blank=True, null=True, related_name='+')  # Field name made lowercase.
    sec = models.ForeignKey(Section, models.DO_NOTHING, db_column='sec_ID', blank=True, null=True, related_name='+')  # Field name made lowercase.
    semester = models.ForeignKey(Section, models.DO_NOTHING, db_column='semester', blank=True, null=True, related_name='+')
    year = models.ForeignKey(Section, models.DO_NOTHING, db_column='year', blank=True, null=True, related_name='+')
    grade = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'takes'


class Teaches(models.Model):
    course = models.ForeignKey(Section, models.DO_NOTHING, db_column='course_ID', blank=True, null=True, related_name='+')  # Field name made lowercase.
    sec = models.ForeignKey(Section, models.DO_NOTHING, db_column='sec_ID', blank=True, null=True, related_name='+')  # Field name made lowercase.
    semester = models.ForeignKey(Section, models.DO_NOTHING, db_column='semester', blank=True, null=True, related_name='+')
    year = models.ForeignKey(Section, models.DO_NOTHING, db_column='year', blank=True, null=True, related_name='+')
    dbid = models.ForeignKey(Instructor, models.DO_NOTHING, db_column='ID', blank=True, null=True, related_name='+')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'teaches'

class Func3F19(models.Model):
    name = models.CharField(max_length=20, db_collation='latin1_swedish_ci', blank=True, primary_key=True)
    dept_name = models.CharField(max_length=25, db_collation='latin1_swedish_ci', blank=True, null=True)
    studentcount = models.BigIntegerField(db_column='StudentCount', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'func3f19'


class Func3F20(models.Model):
    name = models.CharField(max_length=20, db_collation='latin1_swedish_ci', blank=True, primary_key=True)
    dept_name = models.CharField(max_length=25, db_collation='latin1_swedish_ci', blank=True, null=True)
    studentcount = models.BigIntegerField(db_column='StudentCount', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'func3f20'


class Func3S19(models.Model):
    name = models.CharField(max_length=20, db_collation='latin1_swedish_ci', blank=True, primary_key=True)
    dept_name = models.CharField(max_length=25, db_collation='latin1_swedish_ci', blank=True, null=True)
    studentcount = models.BigIntegerField(db_column='StudentCount', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'func3s19'


class Func3S20(models.Model):
    name = models.CharField(max_length=20, db_collation='latin1_swedish_ci', blank=True, primary_key=True)
    dept_name = models.CharField(max_length=25, db_collation='latin1_swedish_ci', blank=True, null=True)
    studentcount = models.BigIntegerField(db_column='StudentCount', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'func3s20'

class Func4F(models.Model):
    course_id = models.CharField(max_length=8, db_collation='latin1_swedish_ci', primary_key=True)
    sec_id = models.CharField(max_length=3, db_collation='latin1_swedish_ci')
    sectionedstudents = models.BigIntegerField(db_column='sectionedStudents', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'func4f'


class Func4S(models.Model):
    course_id = models.CharField(max_length=8, db_collation='latin1_swedish_ci', primary_key=True)
    sec_id = models.CharField(max_length=3, db_collation='latin1_swedish_ci')
    sectionedstudents = models.BigIntegerField(db_column='sectionedStudents', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'func4s'