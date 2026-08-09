# 选项
## 读取选项

将导入添加到服务中（确保相对路径正确）：

```javascript
import options from "../../services/options.js";
```

然后简单地读取选项：

```javascript
this.firstDayOfWeek = options.getInt("firstDayOfWeek");
```

## 添加新选项

### 复选框选项

参考 `backup.tsx` 中的此示例：

```javascript
export function AutomaticBackup() {
    const [ dailyBackupEnabled, setDailyBackupEnabled ] = useTriliumOptionBool("dailyBackupEnabled");

    return (
        <OptionsSection title={t("backup.automatic_backup")}>
            <FormMultiGroup label={t("backup.automatic_backup_description")}>
                <FormCheckbox
                    name="daily-backup-enabled"
                    label={t("backup.enable_daily_backup")}
                    currentValue={dailyBackupEnabled} onChange={setDailyBackupEnabled}
                />
            </FormMultiGroup>

            <FormText>{t("backup.backup_recommendation")}</FormText>
        </OptionsSection>
    )
}
```

> [!TIP]
> 要触发 UI 刷新（例如 `utils#reloadFrontendApp`），只需将 `true` 作为第二个参数传递给 `useTriliumOption` 方法。