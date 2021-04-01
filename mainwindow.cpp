#include "mainwindow.h"
#include "ui_mainwindow.h"

#include <QDir>
#include <QFile>
#include <QMenu>
#include <QProcess>
#include <QSettings>
#include <QThread>

void MainWindow::createTrayIcon()
{
    QAction *showAction = new QAction(tr("&Show"), this);
    connect(showAction, &QAction::triggered, this, &QWidget::showNormal);

    QAction *quitAction = new QAction(tr("&Quit"), this);
    connect(quitAction, &QAction::triggered, qApp, &QCoreApplication::quit);

    QMenu *trayIconMenu = new QMenu(this);
    trayIconMenu->addAction(showAction);
    trayIconMenu->addAction(quitAction);

    trayIcon = new QSystemTrayIcon(this);
    trayIcon->setContextMenu(trayIconMenu);

    connect(trayIcon, &QSystemTrayIcon::activated, this, &QWidget::showNormal);
    trayIcon->setIcon(QIcon(":/tray.ico"));
    trayIcon->show();
}

QStringList LoadSettings()
{
    QSettings setting("SteamAutoLogin", "settings");
    setting.beginGroup("MainWindow");
    QStringList usernames = setting.value("usernames").value<QStringList>();
    setting.endGroup();

    return usernames;
}

// Setup UI, create tray icon, load settings
MainWindow::MainWindow(QWidget *parent) : QMainWindow(parent), ui(new Ui::MainWindow)
{
    ui->setupUi(this);

    createTrayIcon();

    QStringList usernames = LoadSettings();
    ui->comboBox->addItems(usernames);
}

MainWindow::~MainWindow()
{
    delete ui;
}

void SaveSettings(QComboBox* comboBox)
{
    QStringList usernames;
    for (int i = 0; i < comboBox->count(); i++) {
        QString username = comboBox->itemText(i);
        usernames.append(username);
    }

    QSettings setting("SteamAutoLogin", "settings");
    setting.beginGroup("MainWindow");
    setting.setValue("usernames", usernames);
    setting.endGroup();
}

// Kill steam, change AutoLoginUser, start steam
void MainWindow::on_loginButton_clicked()
{
    system("killall --quiet --wait steam");

    QString username = ui->comboBox->currentText().toLower();
    QFile file(QDir::homePath() + "/.steam/registry.vdf");
    file.open(QIODevice::ReadWrite);
    QByteArray fileData = file.readAll();
    QString text(fileData);
    QRegularExpression re = QRegularExpression("\"AutoLoginUser\".+");
    text.replace(re, "\"AutoLoginUser\"         \"" + username + "\"");
    file.seek(0);
    file.write(text.toUtf8());
    file.close();

    QProcess process;
    process.setProgram("steam");
    process.setStandardOutputFile(QProcess::nullDevice());
    process.setStandardErrorFile(QProcess::nullDevice());
    process.startDetached();

    MainWindow::close();
}

// Remove item from combobox and save
void MainWindow::on_removeButton_clicked()
{
    int index = ui->comboBox->currentIndex();
    ui->comboBox->removeItem(index);

    SaveSettings(ui->comboBox);
}

// Add item to combobox and save
void MainWindow::on_addButton_clicked()
{
    QString username = ui->lineEdit->displayText().toLower();
    ui->comboBox->addItem(username);
    ui->comboBox->setCurrentText(username);
    ui->lineEdit->setText("");

    SaveSettings(ui->comboBox);
}
