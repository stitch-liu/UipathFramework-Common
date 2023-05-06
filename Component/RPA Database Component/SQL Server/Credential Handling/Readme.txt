*SQL server提供加密方法，但需要手动在数据库中添加加密的方式

/****** 创建密钥  ******/
CREATE MASTER KEY ENCRYPTION BY PASSWORD ='passW@ord'
-- passW@ord是初始化密码，可以根据实际情况进行调整
GO

CREATE CERTIFICATE UipathCert with SUBJECT = 'UipathCertificate'
GO

CREATE SYMMETRIC KEY UipathSymmetric WITH ALGORITHM = AES_256
    ENCRYPTION BY CERTIFICATE UipathCert
GO

/***** 以下是加密方式的配置方式与读取方式 *****/
/****** 加密  ******/
OPEN SYMMETRIC KEY UipathSymmetric DECRYPTION BY CERTIFICATE UipathCert;

INSERT INTO [DataTable_Credential]
           ([credenitalName]
           ,[credentialType]
           ,[URL]
           ,[account]
           ,[password]
           ,[port])
     VALUES
           ('武汉依江畔美容有限公司第四分公司'
           ,'湖北省'
           ,N'https://etax.shanghai.chinatax.gov.cn/wszx-web/bszm/apps/views/beforeLogin/indexBefore/pageIndex.html#/'
           ,'91420103MA49QWGC1Q'
		   ,ENCRYPTBYKEY(Key_Guid(N'UipathSymmetric'), 'abc')
           ,'2');

CLOSE SYMMETRIC KEY UipathSymmetric;

GO


/****** 解密  ******/
OPEN SYMMETRIC KEY UipathSymmetric DECRYPTION BY CERTIFICATE UipathCert;

SELECT [credenitalName]
      ,[credentialType]
      ,[URL]
      ,[account]
      ,CAST(DecryptByKey([password]) as varchar(Max)) as Password
      ,[port]
      FROM [DataTable_Credential];

CLOSE SYMMETRIC KEY UipathSymmetric;

GO
